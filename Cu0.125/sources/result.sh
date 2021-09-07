#!/bin/bash

for i in 0 1 2 3
do
 for j in 0 1 2 3 4 5
 do
  cd CUEXCH$i-$j
  #grep TOTEN OUTCAR | tail -1 >> J_INCLD
  echo "$i-$j" >> CHG_MAG  
  grep '   48        ' OUTCAR >> CHG_MAG
  grep '   48       ' OUTCAR >> CHG_MAG
  cd ..
  if [[ $i -eq 0 && $j -eq 0  ]]
  then
   #mv CUSPIN0-$j/J_INCLD .
   mv CUEXCH0-$j/CHG_MAG .
  else
   #cat CUSPIN$i-$j/J_INCLD >> J_INCLD
   cat CUEXCH$i-$j/CHG_MAG >> CHG_MAG
  fi
 done
done

# grep -wvE "text" source > destination
