
# coding: utf-8

import csv
import numpy as np

import os
import nltk
import timeit

pathForSave = "./train/"

def removeSpace(data):
    for index,tok in enumerate(data):
        if tok != '\n':
            data[index] = tok[:-1]
    return data

def openFile(name):
    with open(name, "r") as f:
        return removeSpace([line for line in f])

def partDataToSentences(data):
    indices = [i for i, x in enumerate(data) if x == [] or x=='\n']
    x = 0
    sentences = []
    for i in indices:
        sentences.append(data[x:i])
        x=i+1
    if indices == []:
        return [[data]]
    return sentences


def filterAlfaBeta(tav):
    switcher = {
        'a': 'א',
        'b': 'ב',
        'g': 'ג',
        'd': 'ד',
        'h': 'ה',
        'w': 'ו',
        'z': 'ז',
        'x': 'ח',
        'v': 'ט',
        'i': 'י',
        'k': 'כ',
        'l': 'ל',
        'm': 'מ',
        'n': 'נ',
        's': 'ס',
        'y': 'ע',
        'p': 'פ',
        'c': 'צ',
        'q': 'ק',
        'r': 'ר',
        'e': 'ש',
        't': 'ת',
    }
    func = switcher.get(tav)
    return func != None

def filterOtherTok(tok):
    switcher = ["yyNUMBER",
                'o',
                'yyQUOT',
                'yyCM',
                'yyCLN',
                'yyLRB',
                'yyDOT',
                'yyDASH',
                'yyRRB',
                'yyExcl',
                'yyQM',
                'yySCLN',
                'yyELPS',
                'yyELSE',
                ""]
    return tok in switcher

def checkWord(word):
    flag = False
    for tav in word:
        if not filterAlfaBeta(tav):
            flag = True
    if flag and not filterOtherTok(word):
        return False
    return True

dirs = os.listdir(".")
for dirname in dirs:
    if '_train' in dirname and not os.path.isfile(pathForSave + dirname[:11] + ".train"):
        print dirname[:11]
        start = timeit.default_timer()

        tokens = openFile(dirname)
        tokens_sens = partDataToSentences(tokens)

        good_sens = []
        for index,sen in enumerate(tokens_sens):
            flag = False
            for word in sen:
                if not checkWord(word):
                    flag = True
                    break
            if not flag:
                good_sens.append(sen)

        with open(pathForSave + dirname[:11] + ".train", "w") as text_file:
            for sen in good_sens:
                for tok in sen:
                    text_file.write(tok + '\n')
                text_file.write('\n')

        stop = timeit.default_timer()
        print dirname,stop - start
