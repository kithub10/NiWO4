#!/bin/bash

for i in 0 1 2 3
do
 for j in 0 1 2 3 4 5
 do
  grep -B 1 "  185        " CUSPIN\=3/CUSPIN$i-$j/EIGENVAL >> $i-$j-GAP
  awk 'p{print ($2-p>0) ? ($2-p):'\n'}{p=$2}' $i-$j-GAP | sort -n >> $i-$j-MIN
 done
done
