# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 11:43:16 2018

@author: eleve
"""
import pandas as pd
birddata = pd.read_csv("bird_tracking.csv")
birddata.info()

import matplotlib.pyplot as plt
import numpy as np

ix = birddata.bird_name == "Eric"

x, y = birddata.longitude[ix], birddata.latitude[ix]
plt.figure(figsize=(7,7))
plt.plot(x, y, ".")

# 3 birds path in a single plot
bird_names = pd.unique(birddata.bird_name)
plt.figure(figsize=(7,7))
for bird_name in bird_names:
    ix = birddata.bird_name == bird_name
    x, y = birddata.longitude[ix], birddata.latitude[ix]
    plt.plot(x, y, ".", label=bird_name)
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.legend(loc="lower right")
plt.savefig("3traj.pdf")

"""
np.isnan(speed)
np.isnan(speed).any() # if exists a NAN
np.sum(np.isnan(speed)) # how many NANs
ind = np.isnan(speed)
~ind # bitwise
"""

ix = birddata.bird_name == "Eric"
speed = birddata.speed_2d[ix]
ind = np.isnan(speed)       
plt.hist(speed[~ind])
plt.savefig("hist.pdf")

plt.figure(figsize=(8,4))
speed = birddata.speed_2d[birddata.bird_name == "Eric"]
ind = np.isnan(speed)       
plt.hist(speed[~ind], bins=np.linspace(0, 30, 20), normed=True)
plt.xlabel("2D speed (m/s)")
plt.ylabel("Frequency");
plt.savefig("Speed_Fre.pdf")


# pandas -> do not need to deal with NANs explcitly
birddata.speed_2d.plot(kind="hist", range=[0,30])
plt.xlabel("2D speed");
plt.savefig("pd_hist.pdf")

import datetime

date_str = birddata.date_time[0]
date_str[:-3]

datetime.datetime.strptime(date_str[:-3],"%Y-%m-%d %H:%M:%S")

timestamps = []
for k in range(len(birddata)):
    timestamps.append(datetime.datetime.strptime\
    (birddata.date_time.iloc[k][:-3], "%Y-%m-%d %H:%M:%S"))

birddata["timestamp"] = pd.Series(timestamps, index = birddata.index)

times = birddata.timestamp[birddata.bird_name == "Eric"]
elapsed_time = [time - times[0] for time in times]

elapsed_time[1000]

elapsed_time[1000] / datetime.timedelta(days=1) # show in days
elapsed_time[1000] / datetime.timedelta(hours=1) # show in hours

plt.plot(np.array(elapsed_time) / datetime.timedelta(days=1))
plt.xlabel("Observation")
plt.ylabel("Elapsed time (days)");
plt.savefig("timeplot.pdf")


data = birddata[birddata.bird_name == "Eric"]
times = data.timestamp
elapsed_time = [time - times[0] for time in times]
elapsed_days = np.array(elapsed_time) / datetime.timedelta(days=1)

next_day = 1
inds = []
daily_mean_speed = []
for (i, t) in enumerate(elapsed_days):
    if t < next_day:
        inds.append(i)
    else:
        # compute mean speed
        daily_mean_speed.append(np.mean(data.speed_2d[inds]))
        next_day += 1
        inds = []

plt.figure(figsize=(8, 6))
plt.plot(daily_mean_speed)
plt.xlabel("Day")
plt.ylabel("Mean speed (m/s)")
plt.savefig("dms.pdf")

# 
import cartopy.crs as ccrs
import cartopy.feature as cfeature

proj = ccrs.Meractor()

for name in bird_names:
    ix = birddata['bird_name'] == name
    x, y = birddata.longitude[ix], birddata.latitude[ix]
    ax.plot(x, y, '.', transform=ccrs.Geodetic(), label=name)







