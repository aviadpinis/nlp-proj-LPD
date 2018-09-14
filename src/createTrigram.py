import os
import common
import nltk
import time

path = "./train/"
lib = os.listdir(path)
n=3


with open("./trigram/trigram.lex", "a") as myfile:
    for i,trainFile in enumerate(lib):
        print i

        for idx in xrange(3):
            start = time.time()
            array = common.openFile(path + trainFile)
            size = len(array)
            array = common.partDataToSentences2(array[size*idx:size*(idx+1)])
            print "part1",time.time() - start

            start = time.time()
            for sen in array:
                ngram = nltk.ngrams(sen,n,pad_left=True,pad_right=True, left_pad_symbol='<s>', right_pad_symbol='</s>')
                for gram in ngram:
                    myfile.write(str(gram)+'\n')
            print "part2",time.time() - start

            # start = time.time()
            #
            #
            # with open("./trigram/trigram"+str(i)+"_"+str(size*idx)+".lex", "w") as text_file:
            #     for key in sorted(trigram.keys()):
            #         text_file.write(str(key) + '\t' + str(trigram[key]) + '\n')
            #
            # print "part3:"+str(i)+" "+ str(size*idx),time.time() - start