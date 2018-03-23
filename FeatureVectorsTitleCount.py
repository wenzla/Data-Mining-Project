# I confirmed that csv and re is importable on stdlinux
import csv
import re
import math
from string import digits
import random

count = list()
topic = list()
testsplit = 1900
tempArray = []

#gets character and word count for titles
with open('titles.csv', 'r') as f:
    for line in f:
        wordCount = str(len(line.split()))+" " + str(sum(c != ' ' for c in line))
        count.append(wordCount)

#goes through topics and pulls topics and if none then append none to list and the temp list for training
with open('topics2.csv','r') as f:
    for line in f:
        if line == '\n':
            topic.append('none \n')
        else:
            topic.append(line)


#combines the two list to create a a single feature vector with 2 atributes word count
countVector = list()
for i in range(0, len(topic)):
    output = count[i].strip('\n')+" "+topic[i].strip('\n')
    countVector.append(output)
    tempArray.append(output)

#prints the whole feature vector to screen
print "Start of feature vector: "
for i in range(0, len(countVector)):
    print countVector[i]
print "Finshed printing feature vector..."

#gets first 1900 for training classifer and the last 100 for data
xyPoints = tempArray[:testsplit]
xPoint = list()
yPoint = list()
topic = list()
rp = []
#classifier data set
pointsOfLast = tempArray[testsplit:]

#Save points of first 1900
for i in range(0, len(xyPoints)):
    line = xyPoints[i].split(" ")
    rp.append(tuple([line[0],line[1]]))
    xPoint.append(line[0])
    yPoint.append(line[1])
    topic.append(line[2])

#points for last 100
classxPoint = list()
classyPoint = list()
#save points for classification data set
for i in range(0, len(pointsOfLast)):
    line = pointsOfLast[i].split(" ")
    classxPoint.append(line[0])
    classyPoint.append(line[1])


ResultTopics = []
xy = list()
EuclideanDistance = []
result = []
print "printing distances...."
for x in range(0, len(pointsOfLast)):
    #cordnates for thing that needs to be classfied
    X1 = float(classxPoint[x])
    Y1 = float(classyPoint[x])
    TempEuclideanDistance = [100]
    ty = []
    tx = []

    for i in range(0, len(xyPoints)):
        #cordnates for known
        X2 = float(xPoint[i])
        Y2 = float(yPoint[i])
        point = tuple([0,0])
        distance = math.sqrt((X1 - X2)**2 + (Y1- Y2)**2)
        print distance
        #Gets the shortest distance
        if (distance > 1 and (distance < max(TempEuclideanDistance))):
            TempEuclideanDistance.append(distance)
            point = tuple([str(X2),str(Y2)])

#loops through all topics and matches up data point to
    for a in range(0, len(rp)):
        if point == rp[a]:
            resultingTopc = topics[a]
            result.append(resultingTopc)

        #get the topic based on that point, this is the topic of theu unknown
    #print TempEuclideanDistance
print "printing result"
print result


#opens the avliable topics loop through all and get the topic based on the closest data point
