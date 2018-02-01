#!/usr/bin/python
import sys
import os
import stat
import string
import re
from random import randint

#method extracts first word in the pair
#input: "hello-word"
#output: hello
def extractFirstWord(pairList):
    firstWord = ""
    for char in pairList:
        if char == "-":
            return firstWord
        else:
            firstWord = firstWord + char

#method extracts second word in the pair
#input: "hello-word"
#output: word
def extractSecondWord(pairList):
    secondWord = pairList[(len(extractFirstWord(pairList))+1):(len(pairList))]
    return secondWord
#method checks if the word is the last word in the sentence
def isLastWord(word):
    if word[len(word)-1] == '.':
        return True
    return False




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

joinedString = re.sub('[^a-zA-Z .]+', '', joinedString)
print joinedString
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

#print pairList

while 1:
    str = raw_input("Send: ")
    str = re.sub('[^a-zA-Z .]+', '', str)
    Qword = str.split()[-1]
    #Qword =
    #check if Qword message exist in the text
    counter = 0
    for word in pairList:
        if Qword == extractFirstWord(word):
            counter = 1
    #if not then make Qword = random word in the text
    if counter == 0:
        index = randint(0,len(pairList)-1)
        Qword = extractFirstWord(pairList[index])

    #round will stop at 20
    round = 0
    response = ""
    
    for wordPair in pairList:
        
        if Qword == extractFirstWord(wordPair):
            
            response += extractSecondWord(wordPair) + " "
            #update Qword
            Qword = extractSecondWord(wordPair)
            # if RI ends the sentence
            if isLastWord(Qword) == True:
                break
            else:
                round +=1
                if round == 20:
                    #slice last character
                    response = response[:-1]
                    response += "."
                    break



    # convert first char to upperCase
    response = response[0].upper() + response[1:len(response)]


    print "Receive:", response






