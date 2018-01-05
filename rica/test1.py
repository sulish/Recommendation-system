#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 17:33:58 2017

@author: loki
"""

import pandas as pd
import numpy as np
import folium
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

# Read in earthquake data
#df = pd.read_csv('./file.csv', skiprows = 7)
df = pd.read_csv('./dataset1.csv', skiprows = 7)

# Get the latitude and logitude of the earthquakes
coords = df.as_matrix(columns=['Latitude', 'Longitude'])

# Plot the location of the earthquakes
plt.figure(figsize = (12, 12))

m = Basemap(projection='merc', resolution='l', epsg = 4269, 
            llcrnrlon=-122.7,llcrnrlat=36.2, urcrnrlon=-120.8,urcrnrlat=37.5)

# plot the aftershock
x, y = m(coords[:, 1], coords[:, 0])
m.scatter(x,y,5,marker='o',color='b')
m.arcgisimage(service='World_Shaded_Relief', xpixels = 5000, verbose= False)
    
plt.show()

