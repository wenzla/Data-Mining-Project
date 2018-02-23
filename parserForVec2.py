#I used beautifulsoup to parse through the file. Managed to separate the topics (class labels) and the bodies.
#This needs to be cleaned up a lot. Thought of having another xml with both the content and the topic labels

'''
So far this parser creates a csv file called titles.csv.
In this file, the format is as follows:

Line: Each line represents which .sgm file it comes from i.e. each file gets its own line

Comma-separated-value: each csv is the titles for each article; if blank, no titles were listed;
multiple titles separated by whitespace.

'''

from xml.etree import ElementTree
import re
from io import StringIO

import bs4
from bs4 import BeautifulSoup
import os
fileDir = os.path.dirname(os.path.realpath('__file__'))
# The number below changes which files to parse. Use 22 to run all files
numberOfFiles = 22

# This function just makes it so we can iterate through the files so we don't have to run it
# over and over again.
def makeString(counter):
	returnString = ""
	if counter < 10:
		returnString = str(0) + str(counter)
	else:
		returnString = '' + str(counter)
	return returnString

# Actually parses the file given a filename, commented out lots of lines of code that can be used for other tags
def parseFile(filename):
	f = open(filename, 'r')
	filetext = f.read()
	totstring=""
	for x in filetext:
		string=re.sub("[^0-9a-zA-Z<>/\s=!-\"\"]+","", x)
		totstring+=string
		#END FOR
	soup = BeautifulSoup(totstring, "html.parser")
	#print(soup.prettify())
	#bodies = list()
	#topics = list()
	#places = list()
	titles = list()
	#bodies=soup.findAll("body")
	#topics=soup.findAll("topics")
	#places=soup.findAll("places")
	titles=soup.findAll("title")

	#tags = list()
	#for item in soup.findAll('reuters'):
	 #   tags.append(item['lewissplit'])
	#print(tags[0])
	outputstring=""
	#for topic in topics:
	#print(topic.text)
	print "Finished reading " + dataname
	for x in range(0,len(titles)):
		for title in titles[x]:
			outputstring=outputstring + title + " "
		#End For
		outputstring=outputstring + ","
	#End For
	#print (outputstring)
	# Trims the last comma off of the outputstring
	outputstring=outputstring[:-1] + "\n"
	outfile.write(outputstring)

'''ACTUAL START OF APPLICATION'''
outfile=open("titles.csv","w")
for counter in range (0,numberOfFiles):
	dataNameString = makeString(counter)
	dataname='Data/reut2-0' + dataNameString + '.sgm'
	filename = os.path.join(fileDir, dataname)
	print "Reading " + dataname + "... "
	parseFile(filename)
#End For

outfile.close()


#if topics[x].text=="":
#			continue
#		outputstring=outputstring+"<TOPICS>"+topics[x].text+"</TOPICS>\n"+"<BODY>"+bodies[x].text+"</BODY>\n"
