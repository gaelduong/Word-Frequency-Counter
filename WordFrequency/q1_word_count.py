#!/usr/bin/python
import re #regex
import sys
import os
import string
import stat




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

#get rid of all non-alphabetic characters
joinedString = re.sub('[^a-zA-Z ]+', '', joinedString)

#joinedString = joinedString.replace('[^a-zA-Z]','')

#split the string into individual words
wordList = joinedString.split()

#print wordList
dictionary = {}
for word in wordList:
    #if word already in dictionary, frequenct ++
	if word in dictionary:
		dictionary[word] += 1
    # if not then add it to dictionary and set frequency = 1
	elif word not in dictionary:
		dictionary[word] = 1

for Word, frequency in sorted(dictionary.iteritems(), key=lambda (k,v): (v,k), reverse = True):

    print "%s:%s" % (Word, frequency)



