#!/usr/bin/python3

# import the smart plug library
from pyHS100 import SmartPlug, Discover
from pprint import pformat as pf

# datetime standard functions
import time
import datetime

# to manipulate files
import os

# ===== discover the meter to use
print("searching for a smart plug in the network...")
devices = Discover.discover(timeout=1)
# print(devices)

meterIP = None
for ip, device in devices.items():
    if isinstance(device, SmartPlug):
        print("will use the smart meter discovered on:", ip)
        print(device)
        print()
        meterIP = ip

if meterIP is None:
    quit("no meter discovered on the network")


# ===== connect the plug
plug = SmartPlug(meterIP)

# print info
#print("Hardware: %s" % pf(plug.hw_info))
#print("Full sysinfo: %s" % pf(plug.get_sysinfo())) # this prints lots of information about the device

#print("Per day: %s" % plug.get_emeter_daily(year=2018, month=3))
#print("Per month: %s" % plug.get_emeter_monthly(year=2018))

#print("Current consumption: %s" % plug.get_emeter_realtime())

# create a file 
filename = "measured_%s.csv"  % datetime.datetime.now().strftime("%Y_%m_%d-%H_%M_%S")


print("the measures will be stored in file: ", filename)

try:
    os.unlink("lastgraph.csv")
except:
    # ignore it
    pass
try:
    os.symlink(filename, "lastgraph.csv")
    print("you also can find the same content in link: lastgraph.csv")
except e:
    # ignore it
    print(e)

print()
print("to graph the data, use: gnuplot draw.gnuplot")
print()
print("to stop data recording, just hit Ctrl+C")


# open the file to write into it
with open(filename, 'a') as f:
    
    # write headers    
    f.write("year;month;day;hour;minute;seconds;timestamp;") 
    f.write("power;current;voltage;total\n")
    f.flush()
    os.fsync(f)


    # loop forever
    while True:
        consumption = plug.get_emeter_realtime()

        now = datetime.datetime.now()
        f.write("%i;%i;%i;" % (now.year, now.month, now.day))
        f.write("%i;%i;%i;" % (now.hour, now.minute, now.second))
        f.write("%f;" % now.timestamp())
                
        f.write("%f;" % consumption['power'])
        f.write("%f;" % consumption['current'])
        f.write("%f;" % consumption['voltage'])
        f.write("%f\n" % consumption['total'])

        f.flush()

        # wait a bit
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            quit("\nbye ;-)")
    
