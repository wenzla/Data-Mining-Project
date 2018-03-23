# DataMining

OSU CSE data mining class project

Application written in python

Group members:
Allen Wenzl
Kevin Truong

How to run: 
With the submission, we have given you the parsed files need for the program to run (the csv files).

1) >> python FeatureVectorsPart2.py

Note: This command takes a while as it generates feature vectors then builds two classification models.

The above command is used to generate feature vectors such that it is the occurrences of the most popular words used in the titles overall weighted by TF/IDF and has each topic word removed from it.
The word/blank after each feature vector is the topic the article is classified under. These can be viewed in FV1.txt

The classifications can be viewed on the console after the above command is run.
 
 
 
Files being submitted:

FeatureVectorsPart2.py - This is the file that generates classifications of one feature vector (as described in how to run 1)
README.md - This file.
titles.csv - The list of titles of the first 2000 articles in the dataset
topics.csv - The list of all topics in the entire dataset
topics2.csv - The list of all topics in the first 2000 articles in the dataset
