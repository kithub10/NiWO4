#!/bin/bash

for i in 0 1 2 3
do
 for j in 0 1 2 3 4 5
 do
  cp split_dos CUSPIN\=3/CUSPIN$i-$j
  cd CUSPIN\=3/CUSPIN$i-$j
  ./split_dos
  cp ../../dos_afm.gp .; gnuplot dos_afm.gp
  cd ../../
 done
done
