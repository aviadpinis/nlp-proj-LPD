# This baseline is very simple,
# For each word in the sentence, i check if she has LPD
# If it has i choose a random word from the options

# coding: utf-8

import common
from itertools import permutations
import time
import numpy as np
from numpy import unique
import random
import nltk

vocDict = common.getVocabulary()
testSens, answerSens = common.getTestAndAnswerSentences()

# I choose a random word from the options
def randomWord(wordsPossible):
    indexForWordChoice = random.randint(0, len(wordsPossible) - 1)
    return wordsPossible[indexForWordChoice]

# Test baseLine random model
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

# Check result, I check if all the words in the sentence are the same for the expected result.
equals = [results[i] == answerSens[i] for i in xrange(len(answerSens))]

FinalEquals = nltk.FreqDist(equals)
print FinalEquals
print FinalEquals[True]/FinalEquals[False]




