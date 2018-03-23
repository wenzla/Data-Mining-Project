# I confirmed that csv and re is importable on stdlinux
import csv
import re
import math

titles = list()

# gets number of documents with term t in it (divisor in idf formula)
idf = {}
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
topics = []
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
		# the below line is so the tf-idf removes all topics too
		word_counter.pop(topic)
	except ValueError:
		pass
	#End Try	
#End For

total_num_docs = 2000
tf_idf = []
TitleFV = list()
outputfile=open("FV1.txt","w")

# Calculates tf-idf
with open('titles.csv', 'r') as f:
    for line in f:
		words_in_line = re.findall(r'\w+', line)
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
			outputstring = ' '.join(str(e) for e in TitleFV[len(TitleFV)-1]) + ' , ' + topic[len(TitleFV)-1] +  '\n'
			outputfile.write(outputstring)
		#End if
	#End for
#End with

print(len(titles))

outputfile.close()

'''
TitleFV = list()

I know this is an abomination, but it works
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
		TitleFV.append(elementArray)
	#End For
#End For

#Test
print(len(titles))'''
