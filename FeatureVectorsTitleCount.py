# I confirmed that csv and re is importable on stdlinux
import csv
import re
import math


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
for i in range(0, len(countVector)):
    print countVector[i]

#gets first 1900 for training classifer and the last 100 for data
xyPoints = tempArray[:testsplit]
xPoint = list()
yPoint = list()

#classifier data set
pointsOfLast = tempArray[testsplit:]


#Save points of first 1900
for i in range(0, len(xyPoints)):
    line = xyPoints[i].split(" ")
    xPoint.append(line[0])
    yPoint.append(line[1])

#points for last 100
classxPoint = list()
classyPoint = list()
#save points for classification data set
for i in range(0, len(pointsOfLast)):
    line = pointsOfLast[i].split(" ")
    classxPoint.append(line[0])
    classyPoint.append(line[1])

EuclideanDistance = []
for x in range(0, len(pointsOfLast)):
    #cordnates for thing that needs to be classfied
    X1 = float(classxPoint[x])
    Y1 = float(classyPoint[x])
    TempEuclideanDistance = []

    for i in range(0, len(xyPoints)):
        #cordnates for known
        X2 = float(xPoint[i])
        Y2 = float(yPoint[i])

        distance = math.sqrt((X1 - X2)**2 + (Y1- Y2)**2)
        print distance
        TempEuclideanDistance.append(distance)

    #saves the shortest distance to all

    EuclideanDistance.append(min(TempEuclideanDistance))
    #get min then route it back to the topic of known dataset

print len(EuclideanDistance)

#after routing back to topics, need to figure out accuracy
