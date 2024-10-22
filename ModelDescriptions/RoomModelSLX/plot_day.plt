#!C:\Program Files\gnuplot\bin\gnuplot.exe
set terminal Term linewidth 1.5
set output File

set xlabel 'Model Time [day]' offset 0,0.5

# Line style for axes
set style line 80 lt rgb "#808080"

# Line style for grid, border and tics
set style line 81 lt 0
set style line 81 lt rgb "#808080"
set grid back linestyle 81
set border 3 back linestyle 80
set yrange [*:50<*]
set xtics auto
#set xtics nomirror 1 # per day
set ytics nomirror

set key autotitle columnheader
set key top right box 

# Line styles: try to pick pleasing colors, rather
# than strictly primary colors or hard-to-see colors
# like gnuplot's default yellow.

plot for [i=2:Columns] Trace using ($1/(60*60*24)):(column(i)) with lines ls i
