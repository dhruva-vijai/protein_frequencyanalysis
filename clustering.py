import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
import readfasta

style.use('ggplot')

amino_acids = {'A': 0, 'R': 0, 'N': 0, 'D': 0, 'C': 0,'E': 0, 'Q': 0, 'G': 0, 'H': 0, 'I': 0,'L': 0, 'K': 0, 'M': 0, 'F': 0, 'P': 0,'S': 0, 'T': 0, 'W': 0, 'Y': 0, 'V': 0}

def frequencies(sequence):
    """Return normalized frequency vector (fixes length bias)"""
    counts = np.array([sequence.count(aa) for aa in amino_acids])
    return counts / len(sequence) * 100  # Percent composition


#v is the frequency vector for all amino acid residues



f=input("filename : ")
d=readfasta.read_amino(f)

X=[]

for i in d:
    X.append(frequencies(d[i]))


class Mean_Shift():
    def __init__(self, radius = None, radius_norm_step = 10):  
        self.radius = radius
        self.radius_norm_step = radius_norm_step
    
    def fit(self,data):

        if self.radius == None:
            all_data_centroid = np.average(data,axis=0) 
            all_data_norm = np.linalg.norm(all_data_centroid)
            self.radius = all_data_norm/self.radius_norm_step
            print(self.radius)

        centroids = {}

        for i in range(len(data)):
            centroids[i] = data[i]

        weights = [i for i in range(self.radius_norm_step)][::-1]    
        while True:
            new_centroids = []
            for i in centroids:
                in_bandwidth = []
                centroid = centroids[i]
                
                for featureset in data:

                    distance = np.linalg.norm(np.array(featureset)-np.array(centroid))
                    if distance == 0:
                        distance = 0.00000000001
                    weight_index = int(distance/self.radius)
                    if weight_index > self.radius_norm_step-1:
                        weight_index = self.radius_norm_step-1

                    to_add = (weights[weight_index]**2)*[featureset]
                    in_bandwidth +=to_add

                new_centroid = np.average(in_bandwidth,axis=0)
                new_centroids.append(tuple(new_centroid))

            uniques = sorted(list(set(new_centroids)))

            to_pop = []

            for i in uniques:
                for ii in [i for i in uniques]:
                    if i == ii:
                        pass
                    elif np.linalg.norm(np.array(i)-np.array(ii)) <= self.radius:
                        #print(np.array(i), np.array(ii))
                        to_pop.append(ii)
                        break

            for i in to_pop:
                try:
                    uniques.remove(i)
                except:
                    pass

            prev_centroids = dict(centroids)
            centroids = {}
            for i in range(len(uniques)):
                centroids[i] = np.array(uniques[i])

            optimized = True

            for i in centroids:
                if not np.array_equal(centroids[i], prev_centroids[i]):
                    optimized = False

            if optimized:
                break
            
        self.centroids = centroids
        self.classifications = {}

        for i in range(len(self.centroids)):
            self.classifications[i] = []
            
        for featureset in data:
            #compare distance to either centroid
            distances = [np.linalg.norm(np.array(featureset)-np.array(self.centroids[centroid])) for centroid in self.centroids]
            classification = (distances.index(min(distances)))

            # featureset that belongs to that cluster
            self.classifications[classification].append(featureset)


    def predict(self,data):
        #compare distance to either centroid
        distances = [np.linalg.norm(data[0]-self.centroids[centroid][0]) for centroid in self.centroids]
        classification = (distances.index(min(distances)))
        return classification



clf = Mean_Shift()
clf.fit(X)

centroids = clf.centroids
print(f"Number of clusters: {len(clf.centroids)}")

def show_fixed():
    for cluster_id, members in clf.classifications.items():
        print(f"Cluster {cluster_id}: {len(members)} proteins")

show_fixed()

def prediction(clf,sequence):
    vec=frequencies(sequence)
    distances = [np.linalg.norm(vec - centroid) for centroid in clf.centroids.values()]
    return np.argmin(distances)
    
