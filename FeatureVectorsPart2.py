# I confirmed that csv and re is importable on stdlinux
import csv
import re

titles = list()

#Gets all the words that are used as topics for an article
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
popular_topics = sorted(word_counter, key = word_counter.get, reverse = True)

#Gets all the words that are used as titles for an article
with open('titles.csv', 'r') as f:
    text = f.read()
words = re.findall(r'\w+', text)
word_counter = {}
for word in words:
	if word in word_counter:
		word_counter[word] += 1
	else:
		word_counter[word] = 1
#End For
popular_titles = sorted(word_counter, key = word_counter.get, reverse = True)

with open('titles.csv', 'r') as csvfile:
	topicReader = csv.reader(csvfile, delimiter=',', quotechar=' ')
	for row in topicReader:
		titles.append(row)
	#End For
#End With

#Gets rid of all the topics in titles
for topic in popular_topics:
	try:
		popular_titles.remove(topic)
	except ValueError:
		pass
	#End Try	
#End For

TopicFV = list()

'''I know this is an abomination, but it works'''
for title in titles:
	for element in title:
		elementArray = list()
		for i in range(0, len(popular_titles)):
			# splits based on whitespace
			vals = element.split()
			# makes a 0 array when there are no titles
			if len(vals) < 1:
				elementArray.append(0)
			else:
				for k in range(0, len(vals)):
					# gets rid of any whitespace if at end of string
					if vals[k].rstrip() == popular_titles[i]:
						elementArray.append(1)
					else: 
						elementArray.append(0)
				#End For
			#End Else
		#End For
		TopicFV.append(elementArray)
	#End For
#End For

#Test
print(TopicFV)
