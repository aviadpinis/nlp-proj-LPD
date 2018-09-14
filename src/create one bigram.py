import numpy as np
import os
import common
import nltk
import time

path = "./bigram/"
lib = os.listdir(path)

bigram = nltk.FreqDist()
for i,bigramfile in enumerate(lib):
    start = time.time()
    print i

    array = common.openFile(path + bigramfile)
    bigram += nltk.FreqDist(array)

    print "part"+str(i),time.time() - start

start = time.time()

with open("./bigram/gram.lex", "w") as text_file:
    for key in sorted(bigram.keys()):
        text_file.write(str(key) + '\t' + str(bigram[key]) + '\n')

print "end all:",time.time() - start