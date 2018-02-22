# I confirmed that csv and re is importable on stdlinux
import csv
import re

topics = list()

#for info on below check out https://stackoverflow.com/questions/3594514/how-to-find-most-common-elements-of-a-list

with open('topics.csv', 'r') as f:
    text = f.read()
words = re.findall(r'\w+', text)
word_counter = {}
for word in words:
	if word in word_counter:
		word_counter[word] += 1
	else:
		word_counter[word] = 1
#End For
popular_words = sorted(word_counter, key = word_counter.get, reverse = True)
top25 = popular_words[:25]

with open('topics.csv', 'r') as csvfile:
	topicReader = csv.reader(csvfile, delimiter=',', quotechar=' ')
	for row in topicReader:
		topics.append(row)
	#End For
#End With
	
TopicFV = list()

'''I know this is an abomination, but it works'''
# Makes feature vectors using bag of words model; the dictionary I used was the 25 most common topics.
# The vectors shows which of the most common topics is used for the articles
for topic in topics:
	for element in topic:
		elementArray = list()
		for i in range(0, len(top25)):
			# splits based on whitespace
			vals = element.split()
			# makes a 0 array when there are no topics
			if len(vals) < 1:
				elementArray.append(0)
			else:
				for k in range(0, len(vals)):
					# gets rid of any whitespace if at end of string
					if vals[k].rstrip() == top25[i]:
						elementArray.append(1)
					else:
						elementArray.append(0)
				#End For
			#End Else
		#End For
		TopicFV.append(elementArray)
	#End For
#End For

print (TopicFV)