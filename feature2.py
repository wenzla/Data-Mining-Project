from xml.etree import ElementTree
import re
from io import StringIO
import csv
import bs4
from bs4 import BeautifulSoup
import os
fileDir = os.path.dirname(os.path.realpath('__file__'))
numberOfFiles = 1
def makeString(counter):
	returnString = ""
	if counter < 10:
		returnString = str(0) + str(counter)
	else:
		returnString = '' + str(counter)
	return returnString
	
# Actually parses the file given a filename, commented out lots of lines of code that can be used for other tags
def parseFile(filename,word1):
    f=open(filename,'r')
    filetext=f.read()
    totstring=""
    for x in filetext:
        string=re.sub("[^0-9a-zA-Z<>/\s=!-\"\"]+","", x)
        totstring+=string
    soup=BeautifulSoup(totstring,"html.parser")
    bodies=list()
    topics=list()
    bodies=soup.findAll("body")
    topics=soup.findAll("topics")
    word=list()
    word1=[]
    word2=list()
    print("Finished reading ",dataname)
    for x in range(0,len(bodies)):
        for body in bodies[x]:
            
            word=body.split()
            #print(word)
            word2.append(word)
            word1=word1+word
 
    #print(word1)
   # vocab=list()
    #for sublist in word1:
     #   for item in sublist:
      #      vocab.append(item)
       #     print(vocab)
    #print("vocab",len(vocab))
    with open("csvfile47.csv", "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        for x in range(0,len(bodies)):
            for val in word:
                writer.writerow([val]) 
        
    dic = countWords(word1)
    sorted_items=sorted(dic.items())
    #print(dic)
    
    #dic2=countWords(vocab)
    
    print(word1[1:10])
    #sorted_items=sorted(dic2.items())
    for x in range(0,len(bodies)):
        for wordsx in word2:
            bg=bagofwords(wordsx,word1)
            print(bg)
   
    
def countWords(A):
   dic={}
   
   for x in A:
       if not x in  dic:        #Python 2.7: if not dic.has_key(x):
          dic[x] = A.count(x)
   return dic
import numpy as np
def bagofwords(sentence, words):
    #sentence_words = extract_words(sentence)
    # frequency word count
    bag = np.zeros(len(words))
    for sw in sentence:
        for i,word in enumerate(words):
            if word == sw: 
                bag[i] += 1
                
    return np.array(bag)

for counter in range(0,numberOfFiles):
    dataNameString = makeString(counter)
    dataname='C:\\Users\\sunil\\Downloads\\reuters\\reuters21578.tar\\reut2-0'+dataNameString+ '.sgm'
    filename=os.path.join(fileDir,dataname)
    print("Reading ",dataname,"....")
    word1=list()
    parseFile(filename,word1)
    
#for words in word1:
 #   x=bagofwords(words,word)
  #  print(x)


    
#End For
	

        
