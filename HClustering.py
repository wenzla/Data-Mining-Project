# I confirmed that csv and re is importable on stdlinux
import csv
import re
import math
import random

total_num_docs = 128
tf_idf = []
TitleFV = list()
outputfile=open("FV1.txt","w")
topics = []
testTopics = []
testTitles = []
idf = {}
word_count = {}

def getCentroid(array1, array2):
    centroid = []
    for i in range(0,len(array1)):
        x = (array1[i]+array2[i])/2
        centroid.append(x)
    #end for
    return centroid
#end def

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
    return sIndex, smallest
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
            distance = math.sqrt(distance)
            distances.append(distance)
        #End for
        EuclideanDistance.append(distances)
    #end for
    return EuclideanDistance
#End def

'''Start of Application'''
# gets number of documents with term t in it (divisor in idf formula)
with open('titles.csv', 'r') as f:
    for line in f:
        words_in_line = re.findall(r'\w+', line)
        used_words = []
        for word in words_in_line:
            if word not in used_words:
                if word in idf:
                    idf[word] += 1
                else:
                    idf[word] = 1
                #End if
            #End if
            used_words.append(word)
        #End if
    #End for
#End with

#Gets all the words that are used as topics for an article
tempArray = []
with open('topics2.csv', 'r') as f:
    for line in f:
        tempArray.append(line)
    #End for
#End open

topics = tempArray

words = re.findall(r'\w+', ''.join(topics))
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
#End For
popular_topics = sorted(word_count, key = word_count.get, reverse = True)

tempArray = []
#Gets all the words that are used as titles for an article
with open('titles.csv', 'r') as f:
    for line in f:
        tempArray.append(line)
    #end for
#end open
text = tempArray

words = re.findall(r'\w+', ''.join(text))
word_counter = {}
total_words = 0
for word in words:
    total_words += 1
    if word in word_counter:
        word_counter[word] += 1
    else:
        word_counter[word] = 1
#End For
popular_words = sorted(word_counter, key = word_counter.get, reverse = True)
popular_titles = popular_words[:500]
# print popular_titles

tempArray = []
with open('titles.csv', 'r') as f:
    for line in f:
        tempArray.append(line)
    #End for
#End open

text = tempArray

# Creating matrices used for classification 
for a in range(0,len(text)):
    words_in_line = re.findall(r'\w+', text[a])
    length = len(words_in_line)
    title_words = {}
    if length > -1:
        # gets words in each line
        for word in words_in_line:
            if word in title_words:
                title_words[word] += 1
            else:
                title_words[word] = 1
            #End if
        #End for
        # the actual calculation
        tf_feature = {}
        for word in title_words:
            tf_feature[word] = ((float(title_words[word])/length) * (math.log10(total_num_docs/idf[word])))
        #End for
        tf_idf.append(tf_feature)
        
        for word in words_in_line:
            elementArray = list()
            for i in range(0, len(popular_titles)):
                # splits based on whitespace
                vals = word.split()
                # makes a 0 array when there are no titles
                if len(vals) < 1:
                    elementArray.append(0)
                else:
                    for k in range(0, len(vals)):
                        # gets rid of any whitespace if at end of string
                        if vals[k].rstrip() == popular_titles[i]:
                            x = tf_idf[len(tf_idf)-1][vals[k]]
                            elementArray.append(x)
                        else: 
                            elementArray.append(0)
                    #End For
                #End Else
            #End For
        #End For
        TitleFV.append(elementArray)
        if len(TitleFV)-1 < total_num_docs: 
            outputstring = ' '.join(str(e) for e in TitleFV[len(TitleFV)-1]) + ' , ' + topics[len(TitleFV)-1]
            outputfile.write(outputstring)
        #end if
    #End if
#End for

print "Feature vectors created..."

distances = getDistances(TitleFV)
Clusters = TitleFV
ClusterIndex = []
for i in range(0,len(Clusters)):
    ClusterIndex.append(i)
#end for

# Loops until there is only 'one' node in the tree
while len(Clusters) > 1:
    for i in range(0,len(Clusters) - 1):
        # If I do not include this seemingly redundant if statement, it just fails
        if i < len(Clusters) - 1:
            # Finds the vector which has the smallest euclidean distance (ties are broken by index order)
            firstFV = Clusters[i]
            candidateCluster = getLowestDistance(distances[i], i)
            pointIndex = Clusters.pop(candidateCluster[0])
            x = ClusterIndex.pop(candidateCluster[0])
            # Make the cluster a tuple of the indexes
            ClusterIndex[i] = ClusterIndex[i], x
            #Creates a new centroid vector to do distance calculations to
            Clusters[i] = getCentroid(pointIndex, firstFV)
            #Redo distance calculations since  
            distances = getDistances(Clusters)
            print candidateCluster
        #end if
    #end for
#end while
print ClusterIndex






