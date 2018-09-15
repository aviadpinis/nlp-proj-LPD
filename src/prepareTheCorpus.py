
# coding: utf-8

import os
import xml.etree.ElementTree as ET
import common

# location files for corpus
pathXmlFiles = '../data/'
pathForSaveNewFiles = "../textTrain/"
pathForSaveFileCorpus = "./train/"

# The corpus divided into ten parts
# For all files from each part, i export all sentencs into one file.
dirs = os.listdir(pathXmlFiles)
for idx,dirname in enumerate(dirs):
    print idx
    tokens = []
    if os.path.isdir(pathXmlFiles+dirname):
        files = os.listdir(pathXmlFiles + dirname)
        for filename in files:
            if os.stat(pathXmlFiles+dirname+ '/'+filename).st_size > 0 and filename != 'index.html':
                tree = ET.parse(pathXmlFiles + dirname + '/' + filename)
                root = tree.getroot()

                for article in root:
                    if article.tag == 'article':
                        for paragraph in article:
                            if paragraph.tag == 'paragraph':
                                for sentence in paragraph:
                                    for token in sentence:
                                        tokens.append(token.get('transliterated'))
                                    tokens.append('\n')

        with open(pathForSaveNewFiles +dirname+"_train2.txt", "w") as text_file:
            for tok in tokens:
                try:
                    text_file.write(common.switchtSpecialSymobols(tok) + '\n')
                except ValueError:
                    text_file.write('yyError' + '\n')

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

# Check if word is okey, and i want to work with.
def checkWord(word):
    flag = False
    for tav in word:
        if not filterAlfaBeta(tav):
            flag = True
    if flag and not filterOtherTok(word):
        return False
    return True

# For all text train files
# For each sentence i check if i can work with them, if i not i jump to the next sentence.
dirs = os.listdir(".")
for dirname in dirs:
    if '_train' in dirname and not os.path.isfile(pathForSaveFileCorpus + dirname[:11] + ".train"):
        tokens = common.openFile(dirname)
        tokens_sens = common.partDataToSentences(tokens)

        good_sens = []
        for index,sen in enumerate(tokens_sens):
            flag = False
            for word in sen:
                if not checkWord(word):
                    flag = True
                    break
            if not flag:
                good_sens.append(sen)

        # Save to new train corpus file
        with open(pathForSaveFileCorpus + dirname[:11] + ".train", "w") as text_file:
            for sen in good_sens:
                for tok in sen:
                    text_file.write(tok + '\n')
                text_file.write('\n')

