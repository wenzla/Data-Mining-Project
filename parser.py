#I used beautifulsoup to parse through the file. Managed to separate the topics (class labels) and the bodies. 
#This needs to be cleaned up a lot. Thought of having another xml with both the content and the topic labels

import arff
from xml.etree import ElementTree
import re
from io import StringIO

import bs4
from bs4 import BeautifulSoup
import os
totstring=""


fileDir = os.path.dirname(os.path.realpath('__file__'))

dataname='C:\\Users\\sunil\\Downloads\\reuters\\reuters21578.tar\\reut2-000.sgm'
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
outfile=open("output.sgm","w")
outfile.write(outputstring)

outfile.close()


