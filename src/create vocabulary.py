
# coding: utf-8

import os
import  common
import nltk

path = "./train/"

# Export all tokens for corpus files
tokens = []

for i,trainFile in enumerate(os.listdir(path)):
    tokens.append(common.openFile(path + trainFile))

# To each token sum, for all tokens
for index,array in enumerate(tokens):
    tokens[index] = nltk.FreqDist(array)

# Unification of all tokens sum from all files.
voc = nltk.FreqDist([])
for index, array in enumerate(tokens):
    print index
    voc += array
    tokens[index] = []

# Save Vocabulat and sum for all token in new file.
with open("vocabulary.lex", "w") as text_file:
    for key in sorted(voc.keys()):
        text_file.write(key + '\t' + str(voc[key]) + '\n')