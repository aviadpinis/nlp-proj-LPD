# coding: utf-8

# Replacing anything taht is not a letter
def switchtSpecialSymobols(tok):
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
        u'א':'a',
        u'ב': 'b',
        u'ג':'g',
        u'ד':'d',
        u'ה':'h',
        u'ו':'w',
        u'ז':'z',
        u'ח':'x',
        u'ט':'v',
        u'י':'i',
        u'כ':'k',
        u'ך':'k',
        u'ל':'l',
        u'מ':'m',
        u'ם':'m',
        u'נ':'n',
        u'ן':'n',
        u'ס':'s',
        u'ע':'y',
        u'פ':'p',
        u'ף':'p',
        u'צ':'c',
        u'ץ':'c',
        u'ק':'q',
        u'ר':'r',
        u'ש':'e',
        u'ת':'t',
        'o': '%',
        '"':' yyQUOT',
        ',':' yyCM',
        ':':' yyCLN',
        '(':' yyLRB',
        ')':' yyRRB',
        '.':' yyDOT',
        '-':' yyDASH',
        '!':' yyExcl',
        '?':' yyQM',
        ';':' yySCLN',
        '...':' yyELPS'
    }
    return switcher.get(tav)

def switchEndTavInHeb(tav):
    switcher = {
     'כ':'ך',
     'מ':'ם',
     'נ':'ן',
     'פ':'ף',
     'צ':'ץ',
    }
    return switcher.get(tav)

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
        'yyELPS':'...',
        'yyNUMBER':'מספר'
    }
    return switcher.get(tav)
