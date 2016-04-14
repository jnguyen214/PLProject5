#created by Ken and Jimmy on 4/13/16

tokens = ('PROGRAM','COUNTRY', 'SETTING', 'INTEGER')
literals = ['.']

#tokens
t_PROGRAM = r'^Program.*$'
t_COUNTRY = r'^COUNTRY.*$'
t_SETTING = r'^SETTING.*$'

def t_INTEGER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

t_ignore = " \r"

def p_start(t):
    '''start : PROGRAM
             | country
             

    '''

def p_data(t):
    'data : country float INTEGER INTEGER'
    t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4])

def p_float(t):
    'float : INTEGER "." INTEGER'
    t[0] = str(t[1]) + str(t[2]) + str(t[3])

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def p_empty(t):
    'empty : '
    pass

import ply.lex as lex
lexer = lex.lex()

global time_step
time_step = 0

def p_error(t):
    if t == None:
        print("Syntax error at '%s'" % t)
    else:
        print("Syntax error at '%s'" % t.value)

import ply.yacc as yacc #imported from PLY folder
parser = yacc.yacc()

while True:
    try:
        s = raw_input('')
    except EOFError:
        break
    parser.parse(s)

