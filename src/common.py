
# coding: utf-8

import os
import numpy as np
import zipfile

# Const
PATH_VOCABULARY = "./vocabulary.lex"
PATH_SENTENCES_WITH_LPD = "./dataWithLPD.gold"
PATH_BIGRAM_MODEL_ZIP= "./bigramModel.zip"
PATH_BIGRAM_MODEL_FILE= "bigramModel.gram"


def getBigramModel():
    model = openFileFromZip(PATH_BIGRAM_MODEL_ZIP,PATH_BIGRAM_MODEL_FILE)
    return dict([row.split('\t') for row in model])

# vocabulary for check if word is exists
def getVocabulary():
    voc = openFile(PATH_VOCABULARY)
    return dict([row.split('\t') for row in voc])

# Sentences with lpd for test model
# And result sentences for lpd test
def getTestAndAnswerSentences():
    testLpd = openFile(PATH_SENTENCES_WITH_LPD)
    dataTestLPD = np.array([row.split('\t')[0] for row in testLpd])
    testSens = np.array(partDataToSentences(dataTestLPD))

    testAnswer = []
    for row in testLpd:
        if row == '\n':
            testAnswer.append('\n')
        else:
            testAnswer.append(row.split('\t')[1])
    testAnswerSen = np.array(partDataToSentences(testAnswer))
    return testSens,testAnswerSen

def removeSpace(data):
    for index,tok in enumerate(data):
        if tok != '\n':
            data[index] = tok[:-1]
    return data

def openFile(name):
    with open(name, "r") as f:
        return removeSpace([line for line in f])

def openFileFromZip(zipFile,fileName):
    with zipfile.ZipFile(zipFile) as z:
        with z.open(fileName, "r") as f:
            return removeSpace([line for line in f])

def partDataToSentences(data):
    array = np.array(data)
    array = np.split(array,np.where(array == '\n')[0])
    return [np.delete(arr,np.where(arr=='\n')[0]) for arr in array]

# Unknown word smoothing
def smoodUnkFunc(vocDict, limitForSmood):
    keys = vocDict.keys()
    keyForSmooed = [key for key in keys if int(vocDict[key])<limitForSmood]

    for key in keyForSmooed:
        del vocDict[key]

    vocDict['unk'] = limitForSmood
    return vocDict

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
