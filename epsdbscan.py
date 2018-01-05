import csv
import pandas as pd
import numpy as np 
import folium
#from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt 


#baca dataset
df = pd.read_csv('dataset1.csv')
#koordinat latitude dan lot dari dataset
coords = df.as_matrix(columns=['Latitude','Longitude'])

#plot koordinat lokasi dari dataset
plt.figure(figsize=(12,12))		#mengatur ukuran tampilan plot

#m=Basemap(projection='merc',resolution='l',epsg=4269, llcrnrlon=-122.7, llcrnrlat=36.2, urcrnrlon= -120.8, urcrnrlat=37.5)
#x,y = m(coords[:,1], coords[:,0])
#m.scatter(x,y,5,marker='o', color='b')
#m.arcgisimage(service = 'World_Shaded_Relief' ,xpixels=5000, verbose=False)
plt.show()

#insisialisasi awal
import matplotlib.cm as cmx
import matplotlib.colors as colors
from sklearn.cluster import DBSCAN
from sklearn import metrics

kms_per_radian = 6371.0088			#konstanta untuk radius epsilon
epsilon = 1/kms_per_radian

#DBSCAN dengan sklearn
db=DBSCAN(eps=epsilon, min_samples=5, algorithm='ball_tree',metric='haversine').fit(np.radians(coords))

cluster_labels = db.labels_
n_clusters = len(set(cluster_labels))

#cluster_labels = -1 artinya data oulier

cluster = \
	pd.Series([coords[cluster_labels == n] for n in range(-1,n_clusters)])


#optional, function untuk memberikan warna berbeda setiap cluster
def get_cmap(N):
	color_norm = colors.Normalize(vmin=0,vmax=N-1)
	scalar_map = cmx.ScalarMappable(norm=color_norm,cmap='nipy_spectral')
	def map_index_to_rgb_color(index):
		return scalar_map.to_rgba(index)
	return map_index_to_rgb_color

#untuk plot hasil akhir clustering
plt.figure(figsize=(12,12))
#m=Basemap(projection='merc',resolution='l',epsg=4269, llcrnrlon=-122.7, llcrnrlat=36.2, urcrnrlon= -120.8, urcrnrlat=37.5)

unique_label=np.unique(cluster_labels)

#memangil function untuk warna yang berbeda
cmaps = get_cmap(n_clusters)

#plot beberapa cluster. Hitam ialah outlier
for i, clus in enumerate(clusters):
	lons_select = cluster[:,1]
	lats_select = cluster[:,0]
	x,y = m(lons_select,lats_select)
	#m.scatter(x,y,5,marker='o',color=cmaps(i),zorder=10)

#m.arcgisimage(service='World_Shaded_Relief', xpixels=5000,verbose=False)
plt.show()