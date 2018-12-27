ABSTRACT---Clustering is an automatic learning technique aimed at grouping a set of objects into subsets or clusters. Websites clustering aims to automatically group related websites into clusters. The  main  emphasis  is  to  cluster  with  a  high  accuracy  as possible going through set of links given. In this paper an attempt is made to cluster datascience related websites using different clustering algorithms.

INTRODUCTION--

The websites having content related to datascience are increased a lot. Different websites have contents on topics related to datascience. It is becoming difficult for a datascience enthusiast to decide which website to learn datascience topics. 

In this regard this paper aims at clustering of specified datascience related websites and labelling the webiste clusters. This helps the datascience enthusiast to get the websites list related to the required datascience topic and to learn the topic.

Clustering is done by providing a list of datascience websites obtained via a survey and the terms or words related to datascience are also provided. Data from the websites is collected using scraping. Here scraping is done using scrapy tool in python. Data from the websites is converted to a vector containing frequency of each datascience reated keyword.

LITERATURE SURVEY---

CLUSTERING USING K-MEANS--

K-Means algorithm was proposed in the  year 1957  by Stuart  Lloyd. The k-means clustering algorithm is known to  be efficient  in clustering  large data sets. This clustering algorithm is one of the simplest and  the  best  known unsupervised  learning  algorithms. K-Means algorithm aims at partitioning a set of objects in to k number of clusters, where k could be a pre-defined or user-defined constant. K-Means algorithm clusters objects based on theit properties. It defines k centroids, one centroid for each cluster. It is ensured that the centroid is nearer to all the objects in that cluster.

K-Means algorithm first assumes(randomly) k number of centroids and tries to add each object to the cluster whose centroid is nearest to the object. After adding all the objects to cluster, cluster centroid is recalculated. This process is iterated until no object is reassigned to a new cluster in the above process. 

The term frequency vector for each webiste an be compared similarly to Tf-Idf matrix. This n-dimensional data is converted to two dimensions using MDS(Multi Dimensional Scaling).

This two dimensional data is fed to K-Means algorithm to cluster the websites. 


CLUSTERING USING HIERARCHICAL CLUSTERING ALGORITHM----

Hierarchical clustering is used here in a agglomerative way. This algorithm clusters objects based on their distance between them. Each object is assumed to be a cluster intially, and then it starts merging objects in to a single cluster if they are nearer to each other. In this way this algorithm clusters the objects. This clustering does not require number of clusters i.e. k value in case of K-Means. The clusters obtained by this algorithm are related to each other in a hierarchical pattern.

In this case the distance between each webiste is calculated using cosine similarity/ cosine distance calculation. Cosine distance is calculated using the frequency vectors of each webiste.








Step 1:  Choose the words which are related to datascience and used as terms for clustering
Step 2:  Choose the list of websites which are considered for clustering. This websites list is 	 	  obtained by any survey or via google search results.
Step 3:  Crawl a website to get text from it and count the frequencies of the words(if any) choosen 	  in Step-1
Step 4:  Find any hyperlinks in the current page to another webpage of the same webiste and repeat 	  Step-3
Step 5:  Repeat steps 3 and 4 for all the websites considered in Step-2
Step 6:  Cluster the websites by using K-Means and Hierarchical clustering algorithms done similar 	  to document clustering.

PROBLEM STATEMENT AND METHODOLOGY----

EXPERIMENTAL SETUP---

RESULTS AND OBSERVATIONS---

REFERENCES----

