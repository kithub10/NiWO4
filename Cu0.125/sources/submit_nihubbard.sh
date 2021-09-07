#!/bin/bash

# queue request
#$ -q all.q

# pe request
#$ -pe mpi_32 32

# Job name 
#$ -N NiU

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

declare -a spin=('-2 -2  2 -2 -2  2  2  32*0 8*0  3')
declare -a U=('  2.0  0.0  0.0  0.0'\
              '  4.0  0.0  0.0  0.0'\
              '  6.0  0.0  0.0  0.0'\
              '  8.0  0.0  0.0  0.0'\
	      ' 10.0  0.0  0.0  0.0'\
	      ' 12.0  0.0  0.0  0.0'\
              '  3.0  0.0  0.0  0.0'\
              '  5.0  0.0  0.0  0.0'\
              '  7.0  0.0  0.0  0.0'\
              '  9.0  0.0  0.0  0.0'\
	      ' 11.0  0.0  0.0  0.0'\
	      ' 13.0  0.0  0.0  0.0')

# MAGMOM
j=0

# Magnetic calculation
for moment in "${spin[@]}"
do
 i=0
 for value in "${U[@]}"
 do
  mkdir NiU$j-$i
  cp INCAR POSCAR POTCAR KPOINTS NiU$j-$i
  cd NiU$j-$i
  sed -i "s/LDAUU.*/LDAUU        =$value/g" INCAR
  # Magnetic calculation.
  sed -i "s/MAGMOM.*/MAGMOM = $moment/g" INCAR
  if [ $i -gt 5 ]
  then
   sed -i "s/LDAUJ.*/LDAUJ        =  1.0  0.0  0.0  0.0/g" INCAR
  fi
  mpirun -machinefile $TMPDIR/machines -n $NSLOTS ~/bin/vasp_std
  cd ..
  ((i++))
 done
 ((j++))
done
