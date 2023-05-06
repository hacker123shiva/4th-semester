import random
class KMeans:
    def __init__(self,n_cluster=2,max_iter=10):
        self.n_cluster=n_cluster
        self.max_iter=max_iter
        self.centroids=None
    def fit_predicts(self,X):
         random_index=random.sample(range(0,X.shape[0]),self.n_cluster)
         
         for i in range(self.max_iter):
             #assign clusters
             cluster_group=self.assign_clusters(X)
             #move centroids
             # check finish 
    def assign_clusters(self,X):
        return cluster_group



 
