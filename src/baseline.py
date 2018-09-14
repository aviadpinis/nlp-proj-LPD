
# coding: utf-8

import common
from itertools import permutations
import time
import numpy as np
from numpy import unique
import random
import nltk

# const
pathVocabulary = "./vocabulary.lex"
pathLPD = "./dataWithLPD.gold"

# vocabulary for check if word is exists
voc = common.openFile(pathVocabulary)
vocDict = dict([row.split('\t') for row in voc])

#
testLpd = common.openFile(pathLPD)
dataTestLPD = np.array([row.split('\t')[0] for row in testLpd])
testSens = np.array(common.partDataToSentences2(dataTestLPD))

def randomWord(wordPossible):
    indexForWordChoice = random.randint(0,len(wordPossible)-1)
    return wordPossible[indexForWordChoice]

testAnswer = []
for row in testLpd:
    if row == '\n':
        testAnswer.append('\n')
    else:
        testAnswer.append(row.split('\t')[1])

testAnswerSen = np.array(common.partDataToSentences2(testAnswer))

start = time.time()
print "start"
results = []
for sen in testSens:
    newSen = []
    for word in sen:
        if len(word)>9:
        perms = unique([''.join(p) for p in permutations(word)])
        poosWords = []
        if len(perms) > 1:
            for per in perms:
                if per in vocDict and per[0]==word[0] and per[-1]==word[-1]:                    
                    poosWords.append(per)
        if len(poosWords)>0:
            newSen.append(randomWord(poosWords))
        else:
            newSen.append(word)
    results.append(newSen)
print "part2",time.time() - start

equals = [results[i] == testAnswerSen[i] for i in xrange(len(testAnswerSen))]

x = nltk.FreqDist(equals)
print x




