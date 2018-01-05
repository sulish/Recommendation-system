import csv
import numpy as np
from scipy.spatial import distance
from sklearn.cluster import DBSCAN
import pandas as pd

# Pull in our data using DictReader
labels = ['id', 'date_time', 'lat', 'lng','location']
data = csv.DictReader(open('train1.csv', 'r').readlines()[1:], labels)
#df = pd.read_csv('dataset1.csv')

# Separate out the coordinates, which is the only data we care about for now
coords = [(float(d['lat']), float(d['lng'])) for d in data if len(d['lat']) > 0]
coords = [(int(i[location])) for i in data if not(i['location']) > 0]
coords = data.as_matrix(columns=['lat', 'lng'])
print coords

# Scikit-learn's implemenetation of DBSCAN requires the input of a distance matrix showing pairwise
# distances between all points in the dataset.
# distance_matrix = distance.squareform(distance.pdist(coords))

# # Run DBSCAN. Setting epsilon with lat/lon data like we have here is an inexact science. 0.03 looked
# # good after a few test runs. Ideally we'd project the data and set epsilon using meters or feet.
# db = DBSCAN(eps=1.45).fit(distance_matrix)

# # And now we print out the results in the form cluster_id,lat,lng. You can save this to a file and import
# # directly into a mapping program or Fusion Tables if you want to visualize it.
# for k in set(db.labels_):
#     class_members = [index[0] for index in np.argwhere(db.labels_ == k)]
#     for index in class_members:
#         print '%s,%s' % (int(k), '{0},{1}'.format(*coords[index]))
