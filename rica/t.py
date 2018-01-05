#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 17:57:07 2017

@author: loki
"""
import csv
import pandas as pd
import numpy as np
import folium
# from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import matplotlib.cm as cmx
import matplotlib.colors as colors
from sklearn.cluster import DBSCAN
from sklearn import metrics


# Read in earthquake data
df = pd.read_csv('train1.csv', skiprows = 7)
#df = pd.read_csv('./oldTest.csv')
# Get the latitude and logitude of the earthquakes
coords = df.as_matrix(columns=[3,4])


kms_per_radian = 6371.0088
epsilon = 1.5 / kms_per_radian

# Run the DBSCAN from sklearn
db = DBSCAN(eps=epsilon, min_samples=5, algorithm='ball_tree', metric='haversine').fit(np.radians(coords))

cluster_labels = db.labels_
n_clusters = len(set(cluster_labels))

# get the cluster
# cluster_labels = -1 means outliers
clusters = \
    pd.Series([coords[cluster_labels == n] for n in range(-1, n_clusters)])


# define a helper function to get the colors for different clusters
def get_cmap(N):
    '''
    Returns a function that maps each index in 0, 1, ... N-1 to a distinct 
    RGB color.
    '''
    color_norm  = colors.Normalize(vmin=0, vmax=N-1)
    scalar_map = cmx.ScalarMappable(norm=color_norm, cmap='nipy_spectral') 
    def map_index_to_rgb_color(index):
        return scalar_map.to_rgba(index)
    return map_index_to_rgb_color

plt.figure(figsize = (12, 12))
# m = Basemap(projection='merc', resolution='l', epsg = 4269, 
#         llcrnrlon=-122.7,llcrnrlat=36.2, urcrnrlon=-120.8,urcrnrlat=37.5)

unique_label = np.unique(cluster_labels)

# get different color for different cluster
cmaps = get_cmap(n_clusters)

# plot different clusters on map, note that the black dots are 
# outliers that not belone to any cluster. 
# for i, cluster in enumerate(clusters):
#     lons_select = cluster[:, 1]
#     lats_select = cluster[:, 0]
#     x, y = m(lons_select, lats_select)
#     m.scatter(x,y,5,marker='o',color=cmaps(i), zorder = 10)

# m.arcgisimage(service='World_Shaded_Relief', xpixels = 5000, verbose= False)

plt.show()
