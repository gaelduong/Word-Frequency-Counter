#!/usr/bin/python
import sys
import os
import stat
import string
import re

file_name = sys.argv[1]
#open and read txt file
file_object = open(file_name, 'r')
#s is a list
s = file_object.readlines()

trim = ""
joinedString = trim.join(s)

#convert to lower
joinedString = joinedString.lower()

#convert \n to space
joinedString = joinedString.replace('\n',' ')

#get rid of all non-alphabetic chars
joinedString = re.sub('[^a-zA-Z ]+', '', joinedString)

#split string into individual words
aList = joinedString.split()

#get pairs from list, store pairs in pairList 
pairList = []
i = 0
while i < len(aList)-1:

	tempList = [aList[i],aList[i+1]]
	s = "-"
	tempList = s.join(tempList)
	pairList.append(tempList)
	i += 1

#store pairs in dictionary
pairDict = {}
for pair in pairList:
	if pair not in pairDict:
		pairDict[pair] = 1
	else:
		pairDict[pair] += 1

#print pairDict
for Word, frequency in sorted(pairDict.iteritems(), key=lambda (k,v): (v,k), reverse = True):

    print "%s:%s" % (Word, frequency)
