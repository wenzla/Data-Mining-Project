# I confirmed that csv and re is importable on stdlinux
import csv
import re
import math


count = list()
topic = list()

#gets character and word count for titles
with open('titles.csv', 'r') as f:
    for line in f:
        wordCount = str(len(line.split()))+" " + str(sum(c != ' ' for c in line))
        count.append(wordCount)

#goes through topics and pulls topics and if none then append none to list
with open('topics2.csv','r') as f:
    for line in f:
        if line == '\n':
            topic.append('none \n')
        else:
            topic.append(line)

#combines the two list to create a a single feature vector with 2 atributes word count
vector = list()
for i in range(0, len(topic)):
    output = count[i].strip('\n')+" "+topic[i].strip('\n')
    vector.append(output)


for i in range(0, len(vector)):
    print vector[i]
