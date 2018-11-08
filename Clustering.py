import re
import ast
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import cosine_similarity
from scipy.cluster.hierarchy import ward, dendrogram
from matplotlib import pyplot as plt
import pandas as pd
import matplotlib as mpl
from sklearn.manifold import MDS

f = open("scrapedData.txt", "r")

scrapedData = ast.literal_eval(re.search('({.+})', f.read()).group(0))
#dist = 1 - cosine_similarity(tfidf_matrix)
websiteTitles = scrapedData.keys()
seedWords = [word for word in open("seed words.txt","r").readlines()]
data = [d.values() for d in scrapedData.values()]
#print data
termMatrix = np.array(data)
#print termMatrix
dist = 1-cosine_similarity(data)
#print dist

linkage_matrix = ward(dist) #define the linkage_matrix using ward clustering pre-computed distances

fig, ax = plt.subplots(figsize=(15, 20)) # set size
ax = dendrogram(linkage_matrix, orientation="left", labels=websiteTitles)

plt.tick_params(\
    axis= 'x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom= False)

plt.tight_layout() #show plot with tight layout
#plt.show()
#uncomment below to save figure
plt.savefig('ward_clusters.png', dpi=200) #save figure as ward_clusters

#plt.show()

num_clusters = 5

km = KMeans(n_clusters=num_clusters)

km.fit(termMatrix)

clusters = km.labels_.tolist()

print("Top terms per cluster:")
order_centroids = km.cluster_centers_.argsort()[:, ::-1]
terms = seedWords
for i in range(num_clusters):
    print("Cluster %d:" % i),
    for ind in order_centroids[i, :3]:
        print(' %s' % terms[ind]),
    print

MDS()
mds = MDS(n_components=2, dissimilarity="precomputed", random_state=1)
pos = mds.fit_transform(dist)
xs, ys = pos[:, 0], pos[:, 1]

df = pd.DataFrame(dict(x=xs, y=ys, label=clusters, title=websiteTitles))
groups = df.groupby('label')
fig, ax = plt.subplots(figsize=(14, 6)) # set size
ax.margins(0.03) # Optional, just adds 5% padding to the autoscaling

cluster_colors = {0: '#1b9e77', 1: '#d95f02', 2: '#7570b3', 3: '#e7298a', 4: '#66a61e'}
cluster_names = {0: '#1b9e77', 1: '#d95f02', 2: '#7570b3', 3: '#e7298a', 4: '#66a61e'}
for name, group in groups:
    points = ax.plot(group.x, group.y, marker='o', linestyle='', ms=18,
                     label=cluster_names[name], mec='none',
                     color=cluster_colors[name])
    ax.set_aspect('auto')
    labels = [i for i in group.title]

    # set tooltip using points, labels and the already defined 'css'
    #tooltip = mpld3.plugins.PointHTMLTooltip(points[0], labels,
                                            # voffset=10, hoffset=10, css=css)
    # connect tooltip to fig
    #mpld3.plugins.connect(fig, tooltip, TopToolbar())

    # set tick marks as blank
    ax.axes.get_xaxis().set_ticks([])
    ax.axes.get_yaxis().set_ticks([])

    # set axis as blank
    ax.axes.get_xaxis().set_visible(False)
    ax.axes.get_yaxis().set_visible(False)

ax.legend(numpoints=1)  # show legend with only one dot

#mpld3.display()  # show the plot
plt.savefig('kmeans_clusters.png', dpi=200)
plt.show()