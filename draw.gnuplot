# the script can be called like:
#
# gnuplot draw.gnuplot 
# 
# in this case it will just load the file defined below in variable FILE
# 
# or else it can be called like and it will load the file content 
# 
# gnuplot -c draw.gnuplot file_to_plot.txt
# 


# if the argument was defined and exists, then load it
if (exist("ARG1")) {
    FILE = ARG1
}
FILE='lastgraph.csv'

print("will display the content of file ".FILE."\n")
print("will also export the graph in ".FILE.".png\n")

print("to stop the update of the graph, hit Ctrl+C in the console (it's not that easy indeed ^^)")
pause 2


# out data is semicolumn separated
set datafile separator ";"

# x range auto
unset xrange 

# define ranges 
set ytics 5 nomirror tc lt 1
set ylabel 'V' tc lt 1
# automatic range 
unset yrange
#set yrange [210:250]

set y2tics auto nomirror tc lt 2
set y2label 'W' tc lt 2
set y2range [0:*]


plot FILE using 7:8 title 'power' with line, \
     FILE using 7:9 title 'current' with line axes x1y2

# to plot voltage ?     
# FILE using 7:10 title 'voltage' with line 

# replot every second
while (1) {
    replot
    set term push

    set term png 
    set output FILE.".png"
    replot

    set term pop

    pause 1
}



