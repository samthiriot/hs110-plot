# what it it?

If you own a TP-Link HS110 smart plug, that is a plug equiped with a meter, then this provides a script 
to measure the consumption live (every second) and write it into CSV. 

It also comes with a little gnuplot script to plot ugly but informative live graphs. 

# is it reliable?

No. This was done in 1h for fun. It is delivered as it with no guarantee. Have fun of your own! 

It was only tested on Linux. 

# install

## install pyHS100

This just relies on the awesome [the pyHS100 python package](https://github.com/GadgetReactor/pyHS100) to access smart devices. 

It might easily be installed using something like: 
`pip3 install pyHS100` - or maybe `sudo pip3 install pyHS100`

## clone this 

Download this package or  clone the repository. 


## (optional) install gnuplot

If you want to plot the curves using the gnuplot commands, then you better install it. 


# use it 

`python3 pluggy.py` will download data into a novel file. Use Ctrl+C to stop it. 

`gnuplot draw.gnuplot` will plot the data graphically, dynamically and write it into PNG as well. 


