# coding: utf-8

import common
import time
import numpy as np
import nltk

from itertools import permutations

# Init array,and dict
vocDict = common.getVocabulary()
testSens, answerSens = common.getTestAndAnswerSentences()

# Return all possible letter combinations for a word
def perWord(word):
    if len(word) > 3 and len(word) < 9 and not common.filterOtherTok(word):
        return np.unique([''.join(p) for p in permutations(word)])
    else:
        return []

# Get the amount of times a word appeared in corpus
def calcCountWithSmoodUNK(word):
    if word in vocDict:
        return int(vocDict[word])
    else:
        return int(vocDict['UNK'])

# Smood dictionary
vocDict = common.smoodUnkFunc(vocDict,1)

# Run for all sentences in test
# For each sentence, i check for all word if you have more possible letter combinations
# If she has, i check how combination she is the most often in corpus, and chooses it.
results = []
start = time.time()
for sen in testSens:    
    newSen = list(sen[:])
    newSen.insert(0,'<s>')
    newSen.append('</s>')    
    result = []
    for idx in xrange(1,len(newSen)-1):
        perms = perWord(newSen[idx])
        if len(perms) > 1:
            poosWords = []
            for per in perms:
                if per in vocDict and per[0]==newSen[idx][0] and per[-1]==newSen[idx][-1]:
                    poosWords.append(per)                
            path = [calcCountWithSmoodUNK(per) for per in poosWords]
            result.append(poosWords[np.argmax(path)])
        else:
            result.append(newSen[idx])
            
    results.append(result)


# Check result, I check if all the words in the sentence are the same for the expected result.
equals = [results[i] == answerSens[i] for i in xrange(len(answerSens))]

FinalEquals = nltk.FreqDist(equals)
print FinalEquals
print FinalEquals[True]/FinalEquals[False]


