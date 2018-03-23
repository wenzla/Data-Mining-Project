# I confirmed that csv and re is importable on stdlinux
import csv
import re
import math
import random

testsplit = 1900
total_num_docs = 2000
tf_idf = []
TitleFV = list()
outputfile=open("FV1.txt","w")
topics = []
testTopics = []
testTitles = []
idf = {}
word_count = {}

def getProbabilities(class_count):
	classProbabilites = {}
	for e in class_count:
		classProbabilites[e] = (float(class_count[e]))/total_num_docs
	return classProbabilites
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

topics = tempArray[:testsplit]
testTopics = tempArray[testsplit:]

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
text = tempArray[:testsplit]
testTitles = tempArray[testsplit:]

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
popular_titles = popular_words[:1000]

#Gets rid of all the topics in titles
for topic in popular_topics:
	try:
		popular_titles.remove(topic)
		# the below line is so the tf-idf removes all topics too
		word_counter.pop(topic)
	except ValueError:
		pass
	#End Try	
#End For

print("Data handling finished...")

tempArray = []
with open('titles.csv', 'r') as f:
    for line in f:
		tempArray.append(line)
	#End for
#End open

text = tempArray[:testsplit]
testText = tempArray[testsplit:]

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
		if len(TitleFV)-1 < testsplit: 
			outputstring = ' '.join(str(e) for e in TitleFV[len(TitleFV)-1]) + ' , ' + topics[len(TitleFV)-1]
			outputfile.write(outputstring)
		#end if
	#End if
#End for

outputfile.close()
print("Feature vectors created...")

probs = getProbabilities(word_count)
# Makes the conditional probabilities of each attribute
ordered_probs = {}
loop = 0
for prob in probs:
	ordered_probs[loop] = prob
	loop += 1
#end for

rev_order = dict(zip(ordered_probs.values(),ordered_probs.keys()))
conditional_probs = [[0 for col in range(len(popular_titles))] for row in range(len(rev_order))]
# Creates the classifier
for i in range(0,len(TitleFV)):
	# the non zero indexes in the feature vector
	nonZIndex = [];
	for k in range(0,len(popular_titles)-1):
		if TitleFV[i][k] > 0:
			nonZIndex.append(k)
		#end if
	#end for
	topic_array = topics[i].split(',')
	for t in topic_array:
		if t != '\n':
			for z in nonZIndex:
				conditional_probs[rev_order[t]][z] += 1
			#end for
		#end for
	#end for
#end for

print("Done setting up classifier...")
# Uses hold out method to verify accuracy
# Also gets distances to other points
TestFV = list()
Test2FV=  list()
Test_tf = []
for a in range(0,len(testText)):
	words_in_line = re.findall(r'\w+', testText[a])
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
		Test_tf.append(tf_feature)
		
		for word in words_in_line:
			elementArray = list()
			knnArray = list()
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
							x = Test_tf[len(Test_tf)-1][vals[k]]
							knnArray.append(x)
							elementArray.append(1)
						else: 
							knnArray.append(0)
							elementArray.append(0)
					#End For
				#End Else
			#End For
		#End For
		TestFV.append(elementArray)
		Test2FV.append(knnArray)
	#End if
#End for

print("Done setting up test data...")

FVHits = [0] * len(TestFV)
for i in range(0,len(TestFV)):
	# the non zero indexes in the feature vector
	nonZIndex = [];
	for k in range(0,len(popular_titles)-1):
		if TestFV[i][k] > 0:
			nonZIndex.append(k)
		#end if
	#end for
	FVHits[i] = nonZIndex
#end for

guesses = []
epsilon = 0.1
# The classification of the test data occurs here
for i in range(0,len(FVHits)):
	prob_guesses =[0] * len(conditional_probs)
	for j in range(0,len(FVHits[i])):
		for k in range(0,len(conditional_probs)):
			prob_guesses[k] += epsilon
			prob_guesses[k] = ((conditional_probs[k][FVHits[i][j]]) + epsilon) * prob_guesses[k]
		#end for
	#end for
	if (max(prob_guesses)) == 0:
		guesses.append(random.randint(0,len(conditional_probs)-1))
	else:
		guesses.append(prob_guesses.index(max(prob_guesses)))
	#end if
#end for

EuclideanDistance = []
for i in range(0,len(Test2FV)):
	distances = []
	for k in range(0,len(TitleFV)):
		distance = 0
		for j in range(0,len(TitleFV[k])):
			distance += (Test2FV[i][j] - TitleFV[k][j])**2
		#End for
		distances.append(distance)
	#End for
	EuclideanDistance.append(distances)
#end for

#Do the K-nn classification with k = 1
knnOne = []
for i in range(0,len(EuclideanDistance)):
	knnOne.append(topics[EuclideanDistance[i].index(min(EuclideanDistance[i]))])
#End for

print("Done classifying; calculating accuracy...")

"""
print("Guesses:")
for i in range(0,len(guesses)):
	string = "Test Article " + str(i+1) + ": " + ordered_probs[guesses[i]]
	print(string)
#end for
"""

numberCorrect = 0
knnCorrect = 0
# Calculates accuracy of Naive Bayes and 1-nn
for i in range(0,len(testTopics)):
	words = re.findall(r'\w+', testTopics[i])
	if len(words) == 0:
		numberCorrect += 1
		knnCorrect += 1
	else:
		for word in words:
			if word == ordered_probs[guesses[i]]:
				numberCorrect += 1
			#end if
			if word in knnOne[i].split(','):
				knnCorrect += 1
			#end if
		#end for
	#end if
#End for


outstring = 'Naive Bayes Accuracy: ' + str(float(numberCorrect*100)/len(testTopics)) + '%\n1-NN Accuracy: ' + str(float(knnCorrect*100)/len(testTopics)) + '%'
print(outstring)

