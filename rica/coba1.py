"""
dbscan.py
Author: Chase Davis
E-mail: cdavis@cironline.org
Web: http://labs.cironline.org
This is a simple implementation of the DBSCAN clustering algorithm implemented
as closely as possible to the pseudocode laid out in the DBSCAN Wikipedia page:
http://en.wikipedia.org/wiki/DBSCAN
DBSCAN is a popular algorithm for finding clusters in sets of data. Unlike algorithms
such as K-Means, DBSCAN does not require the user to define the number of clusters
in advance. Instead, it locates them based on point density and two inputs: a
search radius and minimum cluster size.
This implementation was designed to be as bare-bones as possible. It borrows from
a couple more robust implementations, which you'll find here:
https://github.com/mrkschan/py-dbscan/
http://code.google.com/p/education-data-ma/source/browse/trunk/data+analysis/clustering/dbscan.js?r=217
Results were checked against test data generated here:
http://people.cs.nctu.edu.tw/~rsliang/dbscan/testdatagen.html
"""
import math

class DBSCAN(object):
    """
    Simple implementation of the DBSCAN algorithm, written to mirror the Wikipedia
    pseudocode as closely as possible: http://en.wikipedia.org/wiki/DBSCAN
    
    d = Full dataset of point instances
    eps = Maximum search radius
    min_pts = The minimum number of points necessary to qualify a cluster
    """
    def __init__(self, d, eps, min_pts):
        self.d = d
        self.dist = self._euclidean
        self.eps = eps
        self.min_pts = min_pts
        self.assigned = []
        self.cluster = []
    
    def run(self):
        """
        Equivalent to the DBSCAN function in the Wikipedia pseudocode.
        """
        self.assigned = [None for i in self.d]
        self.cluster = []
        # for each unvisited point P in dataset D
        for p in range(0, len(self.d)):
            if not self.assigned[p] == None: continue
            # N = regionQuery(P, eps)
            n = self._getNeighbors(p)
            # if sizeof(N) < MinPts
            if len(n) + 1 < self.min_pts:
                # mark P as NOISE
                self.assigned[p] = -1
            else:
                # C = next cluster
                c = len(self.cluster)
                self.cluster.insert(c, [])
                # expandCluster(P, N, C, eps, MinPts)
                self._expandCluster(p, n, c)
            
    def _getNeighbors(self, p):
        """
        Finds close neighbors based on Euclidean distance (although a different distance
        metric could be subbed in with self.distance).
        """
        neighbors = []
        for i in range(0, len(self.d)):
            if i == p: continue
            if self.dist(p, i) <= self.eps:
                neighbors.append(i)
        return neighbors

    def _expandCluster(self, p, n, c):
        """
        Implementation of the expandCluster portion of DBSCAN, written to mirror
        the Wikipedia pseudocode as closely as possible: http://en.wikipedia.org/wiki/DBSCAN
    
        p = Point instance
        n = Full dataset of Point instances
        c = Cluster number
        """
        # add P to cluster C
        self.cluster[c].append(p)
        self.assigned[p] = c
        p_prime = 0
        # for each point P' in N. Note that because N will change within the loop,
        # we need to use a while loop in Python for this to work properly.
        while p_prime < len(n):
            # if P' is not visited
            if self.assigned[n[p_prime]] == None:
                # N' = regionQuery(P', eps)
                n_prime = self._getNeighbors(n[p_prime])
                # if sizeof(N') >= MinPts
                if len(n_prime) + 1 >= self.min_pts:
                    # N = N joined with N'
                    n += [i for i in n_prime if i not in n]
            # if P' is not yet member of any cluster
            if not (self.assigned[n[p_prime]]) > -1:
                # add P' to cluster C
                self.cluster[c].append(n[p_prime])
                # mark P' as visited
                self.assigned[n[p_prime]] = c
            p_prime += 1

    def _euclidean(self, p1, p2):
        """
        Simple implementation of Euclidean ("as the crow flies") distance for
        judging nearest neighbors. Just be sure the p1 and p2 vectors are the
        same length.
        """
        sum = 0
        for i in range((len(self.d[p1]))):
            sum += (self.d[p1][i] - self.d[p2][i]) ** 2
        return math.sqrt(sum)
        
if __name__ == '__main__':
    inputs = ('D:\THESIS\PENELITIAN\DATASET\AGST2009-DES2009/train1.csv')
    with open  (inputs,'r') as a:

    a = DBSCAN(inputs, eps=4, min_pts=6)
    a.run()
    print a.cluster
    print a.assigned
