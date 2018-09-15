
# coding: utf-8

import numpy as np
from itertools import permutations
import common
from random import randint

# const files
pathTrain = "./train/50000-59999.train"
pathVocabulary = "./vocabulary.lex"

# Sentence train files
dataTrain = common.openFile(pathTrain)
sensTrain = common.partDataToSentences(dataTrain)

# Vocabulary for check the proper for new words
vocabulary = set(common.openFile(pathVocabulary))

# For each sentence:
# I start from random place in sentence
# I searce from random start word, word with different letter order.
# If exsit i change and move to the next sentence, else i keep looking.
indexsForModifiedSentences = []
newSentences = []
for indexSourceSentence, sen in enumerate(sensTrain):
    newSen = sen[:]
    randomIndex = randint(0,len(sen))
    for i in range(randomIndex,len(sen)):        
        tok = sen[i]
        if len(tok) > 3 and len(tok) < 12 and not common.filterOtherTok(tok):
            perms = np.unique([''.join(p) for p in permutations(tok)])
            poosWords = []
            if len(perms) > 1:
                for per in perms:
                    if per in vocabulary:
                        poosWords.append(per)                
            for poos in poosWords:
                if poos != tok and poos[0]==tok[0] and poos[-1]==tok[-1]:
                    newSen[i] = poos
                    indexsForModifiedSentences.append(indexSourceSentence)
                    newSentences.append(newSen)
                    break

# Save coprpus test, start with new word, end for source word
with open("dataWithLPD.gold", "w") as text_file:
    for idx, indexSourceSentence in enumerate(indexsForModifiedSentences):
        for indexForWord in xrange(len(newSentences[idx])):
            text_file.write(newSentences[idx][indexForWord] + '\t' + sensTrain[indexSourceSentence][indexForWord] + '\n')
        text_file.write('\n')


