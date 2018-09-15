import numpy as np
import os
import common
import nltk
import time

pathForTrainFiles = "./train/"
lib = os.listdir(pathForTrainFiles)
n=2

bigram = []

for i,trainFile in enumerate(lib):
    start = time.time()
    print i

    array = common.openFile(pathForTrainFiles + trainFile)
    array = np.array(array)
    array = np.split(array,np.where(array == '\n')[0])
    array = [np.delete(arr,np.where(arr=='\n')[0]) for arr in array]
    print "part1",time.time() - start

    start = time.time()
    bigram.append([])
    for sen in array:
        ngram = nltk.ngrams(sen,n,pad_left=True,pad_right=True, left_pad_symbol='<s>', right_pad_symbol='</s>')
        for gram in ngram:
            bigram[i].append(gram)
    print "part2",time.time() - start

    start = time.time()
    bigram[i] = nltk.FreqDist(bigram[i])

with open("./bigram/bigram"+str(i)+".lex", "w") as text_file:
    for key in sorted(bigram.keys()):
        text_file.write(str(key) + '\t' + str(bigram[key]) + '\n')

path = "../bigram/"
lib = os.listdir(path)

bigram = nltk.FreqDist()
for i,bigramfile in enumerate(lib):
    array = common.openFile(path + bigramfile)
    bigram += nltk.FreqDist(array)

with open("../bigramModel.gram", "w") as text_file:
    for key in sorted(bigram.keys()):
        text_file.write(str(key) + '\t' + str(bigram[key]) + '\n')