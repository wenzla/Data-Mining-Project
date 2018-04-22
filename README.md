# DataMining

OSU CSE data mining class project

Application written in python

Group members:
Allen Wenzl
Kevin Truong

How to run: 
With the submission, we have given you the parsed files need for the program to run (the csv files).

1) >> python HClustering.py

Note: This command takes a while as it generates feature vectors and reconstructs distance matrices alot.

The above command is used to generate one heirarchical cluster such that it is the occurrences of the most popular words used in 
the titles overall weighted by TF/IDF and has each topic word removed from it.  The program will output the tuple of 
the closest point along with the distance to the closest point.
The word/blank after each feature vector is the topic the article is classified under. These can be viewed in FV1.txt

The cluster can be viewed on the console after the above command is run.

2) >> python KMeans.python

The above command is used to generate a k=2 KMeans cluster.  The program will output the centroid of each K and the points
at each cluster.
 
Files being submitted:

HClustering.py - This is the file that generates hierarchical clusters of one feature vector (as described in how to run 1) 
KMeans.py - This is the file that generates kmeans clusters of one feature vector (as described in how to run 2) 
README.md - This file.
titles.csv - The list of titles of the first 128 articles in the dataset
topics.csv - The list of all topics in the entire dataset
topics2.csv - The list of all topics in the first 128 articles in the dataset
