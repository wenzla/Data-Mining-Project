#I used beautifulsoup to parse through the file. Managed to separate the topics (class labels) and the bodies. 
#This needs to be cleaned up a lot. Thought of having another xml with both the content and the topic labels

from xml.etree import ElementTree
import re
from io import StringIO

import bs4
from bs4 import BeautifulSoup
import os
totstring=""
fileDir = os.path.dirname(os.path.realpath('__file__'))

# This function just makes it so we can iterate through the files so we don't have to run it
# over and over again.
def makeString(counter):
	returnString = ""
	if counter < 10:
		returnString = str(0) + str(counter)
	else:
		returnString = '' + str(counter)

	#print returnString
	return returnString
	


counter = 0

dataNameString = makeString(counter)
dataname='Data/reut2-0' + dataNameString + '.sgm'
filename = os.path.join(fileDir, dataname)
f = open(filename, 'r')
filetext = f.read()
for x in filetext:
    string=re.sub("[^0-9a-zA-Z<>/\s=!-\"\"]+","", x)
    totstring+=string
#print(totstring)
soup = BeautifulSoup(totstring)
#print(soup.prettify())
bodies = list()
topics = list()
tags = list()

bodies=soup.findAll("body")
#for body in bodies:
 #   print(body.text)
    
topics=soup.findAll("topics")

#for item in soup.findAll('reuters'):
 #   tags.append(item['lewissplit'])

#print(tags[0])
outputstring=""
for topic in topics:
    print(topic.text)
    
for x in range(0,len(bodies)):
    if topics[x].text=="":
        continue
    outputstring=outputstring+"<TOPICS>"+topics[x].text+"</TOPICS>\n"+"<BODY>"+bodies[x].text+"</BODY>\n"
	

#print (outputstring)
outfile=open("output.txt","w")
outfile.write(outputstring)
outfile.close()



	
