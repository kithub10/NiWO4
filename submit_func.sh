#!/bin/bash

# queue request
#$ -q all.q

# pe request
#$ -pe mpi_32 32

# Job name 
#$ -N MATRIX

#$ -S /bin/bash

#$ -V

#$ -cwd

# needs in 
#   $NSLOTS          
#       the number of tasks to be used
#   $TMPDIR/machines 
#       a valid machiche file to be passed to mpirun 
#   enables $TMPDIR/rsh to catch rsh calls if available

echo "Got $NSLOTS slots."
cat $TMPDIR/machines

#######################################################
### MPI JOB
#######################################################
#
#
# Remove all module environments.
 module purge

# Load MPI environments.
 module load intel/18.0.5 sge/8.1.8 vasp/5.4.4

 export OMP_NUM_THREADS=1

 cd $SGE_O_WORKDIR

declare -a arr=("PBE" "PBEsol" "SCAN" "LDA")

for i in "${arr[@]}"
do
 mkdir "$i"
 # KPOINTS vs ENCUT matricize
 for k in 4 8 12 16
 do
  for en in $(seq 200 50 700)
  do
   mkdir "$i"/MATRIX_$k-$en
   cp INCAR POSCAR POTCAR KPOINTS "$i"/MATRIX_$k-$en
   cd "$i"/MATRIX_$k-$en
   echo -e "Automatic mesh\n 0\nGamma\n $k $k $k\n 0 0 0" > KPOINTS
   sed -i "s/ENCUT.*/ENCUT = $en/g" INCAR
   case "$i" in
        "PBE")
         echo "GGA = PE" >> INCAR;;
        "PBEsol")
         echo "GGA = PS" >> INCAR;;
        "SCAN")
         echo "METAGGA = SCAN" >> INCAR;;
        "LDA")
         cp ../../POTCAR_LDA POTCAR;;
        *)
         break;;
   esac
   mpirun -machinefile $TMPDIR/machines -n $NSLOTS ~/bin/vasp_std
   cd ../../
   grep TOTEN "$i"/MATRIX_$k-$en/OUTCAR | tail -1 >> TOTEN;
   sed -e '/4ORBIT/,/ BZINTS/!d' "$i"/MATRIX_$k-$en/OUTCAR >> TOTCHG;
  done
 done
done
