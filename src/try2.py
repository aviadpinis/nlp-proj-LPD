
# coding: utf-8

import os
import xml.etree.ElementTree as ET
import timeit

path = './data/'
dirs = os.listdir( path )
tokens = []

def filter(tok):
    try:
        val = int(tok)
        return "yyNUMBER"
    except ValueError:
        if tok == '%':
            return 'o'
        elif tok == '"':
            return 'yyQUOT'
        elif tok == ',':
            return 'yyCM'
        elif tok == ':':
            return 'yyCLN'
        elif tok == '(':
            return 'yyLRB'
        elif tok == '.':
            return 'yyDOT'
        elif tok == '-':
            return 'yyDASH'
        elif tok == ')':
            return 'yyRRB'
        elif tok == '!':
            return 'yyExcl'
        elif tok == '?':
            return 'yyQM'
        elif tok == ';':
            return 'yySCLN'
        elif tok == '...':
            return 'yyELPS'
        elif tok == '\n':
            return ""
        else:
            return tok

for dirname in dirs:
    if os.path.isdir(path+dirname) and not os.path.isfile(dirname+'_train.txt'):
        start = timeit.default_timer()
        print dirname + ":"
        files = os.listdir( path + dirname)
        for filename in files:
            if os.stat(path+dirname+'/'+filename).st_size > 0 and filename != 'index.html':
                tree = ET.parse(path+dirname+'/'+filename)
                root = tree.getroot()

                for article in root:
                    if article.tag == 'article':
                        for paragraph in article:
                            if paragraph.tag == 'paragraph':
                                for sentence in paragraph:
                                    for token in sentence:
                                        tokens.append(token.get('transliterated'))
                                    tokens.append('\n')

        stop = timeit.default_timer()

        print stop - start
        with open(dirname+"_train.txt", "w") as text_file:
            for tok in tokens:
                try:
                    text_file.write(filter(tok) + '\n')
                except ValueError:
                    print tok
                    text_file.write('yyError' + '\n')

        stop = timeit.default_timer()

        print stop - start





