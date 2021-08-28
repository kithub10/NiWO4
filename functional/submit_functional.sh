declare -a arr=("PBE" "PBEsol" "SCAN" "LDA")

for i in "${arr[@]}"
do
 mkdir "$i"
 cp INCAR POSCAR KPOINTS POTCAR "$i"
 case "$i" in
        "PBE")
         echo "GGA = PE" >> "$i"/INCAR;;
        "PBEsol")
         echo "GGA = PS" >> "$i"/INCAR;;
        "SCAN")
         echo "METAGGA = SCAN" >> "$i"/INCAR;;
        "LDA")
         cp ../POTCAR_LDA "$i"/POTCAR;;
        *)
         break;;
 esac
 cd "$i"
 mpirun -machinefile $TMPDIR/machines -n $NSLOTS ~/bin/vasp_std
 cd ..
done
