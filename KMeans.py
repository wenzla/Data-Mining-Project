# I confirmed that csv and re is importable on stdlinux
import csv
import re
import math
from string import digits
import random

count = list()
topics = list()
testsplit = 1900
tempArray = []

def getCentroid(array1, array2):
    centroid = []
    for i in range(0,len(array1)):
        x = float(array1[i]+array2[i])/2
        centroid.append(x)
    #end for
    return centroid
#end def5

'''
returns a tuple of index, distance
'''
def getLowestDistance(distance_array, index):
    # Largest distance can be is 1
    smallest = 1000.01
    sIndex = 0
    for i in range(0,len(distance_array)):
        candidate = distance_array[i]
        if candidate <= smallest and i != index:
            smallest = candidate
            sIndex = i
        #end if
    #end for
    return sIndex, smalles5t
#end def

'''
Gets the euclidean distances of each element in the array with each other
'''
def getDistances(input_array):
    EuclideanDistance = []
    for i in range(0,len(input_array)):
        distances = []
        for k in range(0,len(input_array)):
            distance = 0
            for j in range(0,len(input_array[k])):
                distance += (input_array[i][j] - input_array[k][j])**2
            #End for
            distance = math.sqrt(float(distance))
            distances.append(distance)
        #End for
        EuclideanDistance.append(distances)
    #end for
    return EuclideanDistance
#End def

#gets character and word count for titles
with open('titles.csv', 'r') as f:
    for line in f:
	wordlen = len(line.split())
	charlen = sum(c != ' ' for c in line)
        wordCount = [wordlen, charlen]
        count.append(wordCount)

#goes through topics and pulls topics and if none then append none to list and the temp list for training
with open('topics2.csv','r') as f:
    for line in f:
        if line == '\n':
            topics.append('none \n')
        else:
            topics.append(line)


#combines the two list to create a a single feature vector with 2 atributes word count
countVector = list()
for i in range(0, len(topics)):
    output = count[i]
    countVector.append(output)
    tempArray.append(output)
#End for

FV = countVector

point1 = [4, 20]
point2 = [8, 40]
Cluster1 = point1
Cluster2 = point2
ClusterPoint1 = []
ClusterPoint2 = []
tempArray.append(point1)
p1Location = len(tempArray) - 1
tempArray.append(point2)
p2Location = len(tempArray) - 1
distances = getDistances(tempArray)

for i in range(0,5):
	for j in range(0, len(FV) - 1):
		candidateP1 = distances[p1Location][j]
		candidateP2 = distances[p2Location][j]
		if candidateP1 < candidateP2:
			Cluster1 = getCentroid(Cluster1, countVector[j])
			if countVector[j] not in ClusterPoint1:
				ClusterPoint1.append(countVector[j])
			#end if
			if countVector[j] in ClusterPoint2:
				ClusterPoint2.pop(ClusterPoint2.index(countVector[j]))
			#end if
		else:
			Cluster2 = getCentroid(Cluster2, countVector[j])
			if countVector[j] not in ClusterPoint2:
				ClusterPoint2.append(countVector[j])
			#end if
			if countVector[j] in ClusterPoint1:
				ClusterPoint1.pop(ClusterPoint1.index(countVector[j]))
			#end if
		#end if
		tempArray.pop()
		tempArray.pop()
		tempArray.append(Cluster1)
		p1Location = len(tempArray) - 1
		tempArray.append(Cluster2)
		p2Location = len(tempArray) - 1
		distances = getDistances(tempArray)	
	#end for
#end for

print 'Centroid of First Cluster: '
print (Cluster1)
print "Points of First Cluster: "
print (ClusterPoint1)
print "Centroid of Second Cluster: "
print (Cluster2)
print "Points of Second Cluster: "
print (ClusterPoint2)







