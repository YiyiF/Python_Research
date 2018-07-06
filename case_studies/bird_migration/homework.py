# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 21:30:16 2018

@author: eleve
"""
import pandas as pd
birddata = pd.read_csv("bird_tracking.csv")
birddata.info()

import matplotlib.pyplot as plt
import numpy as np

ix = birddata.bird_name == "Eric"

# E1

# First, use `groupby()` to group the data by "bird_name".
grouped_birds = birddata.groupby("bird_name")

# Now calculate the mean of `speed_2d` using the `mean()` function.
mean_speeds = grouped_birds.speed_2d.mean()

# Use the `head()` method prints the first 5 lines of each bird.
print(grouped_birds.head())

# Find the mean `altitude` for each bird.
mean_altitudes = grouped_birds.altitude.mean()

# E2

# Convert birddata.date_time to the `pd.datetime` format.
birddata.date_time = pd.to_datetime(birddata.date_time)

# Create a new column of day of observation
birddata["date"] = birddata.date_time.dt.date

# Check the head of the column.
birddata["date"].head()

# Use `groupby()` to group the data by date.
grouped_bydates = birddata.groupby("date")

# Find the mean `altitude` for each date.
mean_altitudes_perday = grouped_bydates.altitude.mean()


# E3
# Use `groupby()` to group the data by bird and date.
grouped_birdday = birddata.groupby(['bird_name','date'])

# Find the mean `altitude` for each bird and date.
mean_altitudes_perday = grouped_birdday.altitude.mean()

# look at the head of `mean_altitudes_perday`.
mean_altitudes_perday.head()

# E4

eric_daily_speed  = grouped_birdday.speed_2d.mean()["Eric"]
sanne_daily_speed = grouped_birdday.speed_2d.mean()["Sanne"]
nico_daily_speed  = grouped_birdday.speed_2d.mean()["Nico"]

eric_daily_speed.plot(label="Eric")
sanne_daily_speed.plot(label="Sanne")
nico_daily_speed.plot(label="Nico")
plt.legend(loc="upper left")
plt.show()









