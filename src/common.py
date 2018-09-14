
# coding: utf-8

import os
import numpy as np

def removeSpace(data):
    for index,tok in enumerate(data):
        if tok != '\n':
            data[index] = tok[:-1]
    return data

def openFile(name):
    with open(name, "r") as f:
        return removeSpace([line for line in f])

def partDataToSentences2(data):
    array = np.array(data)
    array = np.split(array,np.where(array == '\n')[0])
    return [np.delete(arr,np.where(arr=='\n')[0]) for arr in array]

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

def switchtavToSymbol(tav):
    switcher = {
        'o': '%',
        'yyQUOT':'"',
        'yyCM':',',
        'yyCLN':':',
        'yyLRB':'(',
        'yyRRB':')',
        'yyDOT':'.',
        'yyDASH':'-',
        'yyExcl':'!',
        'yyQM':'?',
        'yySCLN':';',
        'yyELPS':'...'
    }
    return switcher.get(tav)

def switchEngHeb(tav):
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
        'o': '%',
        'yyQUOT':'"',
        'yyCM':',',
        'yyCLN':':',
        'yyLRB':'(',
        'yyRRB':')',
        'yyDOT':'.',
        'yyDASH':'-',
        'yyExcl':'!',
        'yyQM':'?',
        'yySCLN':';',
        'yyELPS':'...'
    }
    return switcher.get(tav)

def switchHebToEng(tav):
    switcher = {
        'א':'a',
        'ב': 'b',
        'ג':'g',
        'ד':'d',
        'ה':'h',
        'ו':'w',
        'ז':'z',
        'ח':'x',
        'ט':'v',
        'י':'i',
        'כ':'k',
        'ל':'l',
        'מ':'m',
        'נ':'n',
        'ס':'s',
        'ע':'y',
        'פ':'p',
        'צ':'c',
        'ק':'q',
        'ר':'r',
        'ש':'e',
        'ת':'t',
    }
    return switcher.get(tav)