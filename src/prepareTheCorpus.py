
# coding: utf-8

import os
import xml.etree.ElementTree as ET
import common

# location files for corpus
pathXmlFiles = '../data/'
pathForSaveNewFiles = "../textTrain/"

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


