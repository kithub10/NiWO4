for i in 0 1 2 3
do
 for j in 0 1 2 3 4 5
 do
  grep 'atom =  48' CUSPIN\=3/CUSPIN$i-$j/OUTCAR -A 19 >> $i-$j
  grep 'spin component  2' $i-$j >> $i-$j_ -A 7
  rm -f $i-$j; mv $i-$j_ $i-$j
 done
done
