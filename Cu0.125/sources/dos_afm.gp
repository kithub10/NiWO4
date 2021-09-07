res
set terminal postscript portrait solid enhanced color "Arial-Bold" 12
set output 'dos.eps'
set style line 1 lt 1 lw 2 lc rgb "#C0392B"
set style line 2 lt 1 lw 2 lc rgb "#2980B9"
set style line 3 lt 1 lw 2 lc rgb "#AA0000"
set style line 4 lt 1 lw 2 lc rgb "#8E44AD"
set style line 5 lt 1 lw 2 lc rgb "#F39C12"
set style line 6 lt 1 lw 2 lc rgb "#2C3E50"
set style line 7 lt 1 lw 2 lc rgb "#95A5A6"
set style line 8 lt 1 lw 2 lc rgb "#27AE60"
set style line 9 lt 1 lw 2 lc rgb "#2980B9"
set style line 10 lt 3 lw 2 lc rgb "#000000"

set style fill solid 0.2  

xmin1 =  -8.2
xmax1 =   8.2
ymin1 =    0.0
ymax1 =   40.0
ymin1_1 =  -40.0
ymax1_1 =   40.0
ymin2 =   0.0
ymax2 =   5.0
ymin2_1 =  -0.5
ymax2_1 =   0.5
ymin3 =   0.0
ymax3 =   1.5
ymin3_1 =  -1.25
ymax3_1 =   1.25
xmin2 = -0.12
xmax2 =  0.12

set multiplot

set xzeroaxis
set yzeroaxis
set lmargin 0
set bmargin 0
set tmargin 0
set rmargin 0
unset xlabel 
unset label
unset ylabel 
unset arrow
unset ylabel
set xtics 2 nomirror
set tic scale 0.5

set size 0.80, 0.15
set origin 0.10, 0.78
set xrange [xmin1:xmax1]
set yrange [ymin1_1:ymax1_1]
set title "antiferromagnetic calc."
set format x ""
set format y "%2.0f"
unset xlabel
unset ylabel
unset label
set ytics 10
set label "Total" at graph 0.2, graph 0.90
set key reverse samplen 0.5 spacing 1 at graph 0.95, 0.95
plot 'DOS0'  u 1:($2) w l ls 3 not,\
     'DOS0'  u 1:($3) w l ls 3 not

set origin 0.10, 0.62
unset title                                                                   
unset label
set yrange [ymin2_1:ymax2_1] 
set ytics 2
set label "Ni (red)" at graph 0.4, graph 0.80
set label "Cu (purple)" at graph 0.8, graph 0.80
plot '< paste DOS1 DOS2 DOS3 DOS4 DOS5 DOS6 DOS7' u 1:($10+$12+$14+$16+$18+$29+$31+$33+$35+$37)/7 w l ls 3 not,\
     '< paste DOS1 DOS2 DOS3 DOS4 DOS5 DOS6 DOS7' u 1:($11+$13+$15+$17+$19+$30+$32+$34+$36+$38)/7 w l ls 3 not,\
     '< paste DOS48' u 1:($10+$12+$14+$16+$18+$29+$31+$33+$35+$37) w l ls 3 not,\
     '< paste DOS48' u 1:($11+$13+$15+$17+$19+$30+$32+$34+$36+$38) w l ls 3 not

set origin 0.10, 0.47
unset label
unset ylabel
set yrange [-0.3:0.3]
set label "O" at graph 0.25, graph 0.80 
set ylabel "DOS (states/eV/atom)" offset 1.0,  0
plot '< paste DOS8 DOS9 DOS10 DOS11 DOS12 DOS13 DOS14 DOS15 DOS16 DOS17 DOS18 DOS19 DOS20 DOS21 DOS22 DOS23 DOS24 DOS25 DOS26 DOS27 DOS28 DOS29 DOS30 DOS31 DOS32 DOS33 DOS34 DOS35 DOS36 DOS37 DOS38 DOS39' u 1:($4+$6+$8+$23+$25+$27+$42+$44+$46+$61+$63+$65)/32 w l ls 3 not,\
     '< paste DOS8 DOS9 DOS10 DOS11 DOS12 DOS13 DOS14 DOS15 DOS16 DOS17 DOS18 DOS19 DOS20 DOS21 DOS22 DOS23 DOS24 DOS25 DOS26 DOS27 DOS28 DOS29 DOS30 DOS31 DOS32 DOS33 DOS34 DOS35 DOS36 DOS37 DOS38 DOS39' u 1:($5+$7+$9+$24+$26+$28+$43+$45+$47+$62+$64+$66)/32 w l ls 3 not

set origin 0.10, 0.32
set format x "%2.0f"
unset label
unset ylabel
set yrange [-0.7:0.7]
set ytics 1
set label "W" at graph 0.25, graph 0.80 
set xlabel "Energy (eV)"
plot '< paste DOS40 DOS41 DOS42 DOS43 DOS44 DOS45 DOS46 DOS47' u 1:($10+$12+$14+$16+$18+$29+$31+$33+$35+$37)/8 w l ls 3 not,\
     '< paste DOS40 DOS41 DOS42 DOS43 DOS44 DOS45 DOS46 DOS47' u 1:($11+$13+$15+$17+$19+$30+$32+$34+$36+$38)/8 w l ls 3 not

unset multi
