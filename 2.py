import numpy as np
import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn import metrics

# from sklearn.datasets.samples_generator import make_blobs
# from sklearn.preprocessing import StandardScaler


# #############################################################################
# Generate sample data
X=pd.read_csv('train1.csv')
coords = X.as_matrix(columns=['lat','lng'])
print coords

# #############################################################################
# Compute DBSCAN
#cluster_labels = -1 artinya data oulier
kms_per_radian = 6371.0088
epsilon = 1381.9 / kms_per_radian
# epsilon = 4 / kms_per_radian
db = DBSCAN(eps=epsilon, min_samples=10, algorithm='ball_tree', metric='haversine').fit(np.radians(coords))
core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
core_samples_mask[db.core_sample_indices_] = True
labels = db.labels_


print labels

a = np.matrix(labels)
a_list = list(a.flat)

# print a_list
# b = []
# for row in coords: blajar
#   asd = []
#   for col in row:
#     asd.append(col)
#     # b.append()
#   b.append(asd)

# final_list = []
# for i in xrange(len(b)):
  # final_list.append([b[i],a_list[i]])

with open('train1.csv', 'r') as f:
  i = 0;
  for row in f:
    if 'checkin' not in row:
      form = str(row.replace('\n',''))+','+str(a_list[i])

      print form

      output = open("hasil.csv","a")
      output.write(form+'\n')
      output.close()
      i+=1

# with open('hasil cluster.csv', 'a') as m:  wong blajar
#     m.write(",".join(aaaClass))
#       print row+','+a_list[i]
#       i+=1

# print final_list
# print(list(my_list))

# print(len(list(a.flat)))
# print(len(list(b.flat)))

# Number of clusters in labels, ignoring noise if present.
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
print('Estimated number of clusters: %d' % n_clusters_)

# # #############################################################################
# # Plot result
# import matplotlib.pyplot as plt

# # Black removed and is used for noise instead.
# unique_labels = set(labels)
# colors = [plt.cm.Spectral(each)
#   for each in np.linspace(0, 1, len(unique_labels))]
# for k, col in zip(unique_labels, colors):
#   if k == -1:
#         # Black used for noise.
#     col = [0, 0, 0, 1]

#     class_member_mask = (labels == k)

# xy = X[class_member_mask & core_samples_mask]
# plt.plot((xy[:, 0]), (xy[:, 1]), 'o', markerfacecolor=tuple(col),
#         markeredgecolor='k', markersize=14)

# xy = X[class_member_mask & ~core_samples_mask]
# plt.plot((xy[:, 0]), (xy[:, 1]), 'o', markerfacecolor=tuple(col),
#         markeredgecolor='k', markersize=6)

# plt.title('Estimated number of clusters: %d' % n_clusters_)
# plt.show()

                                                                                                                              
