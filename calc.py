import ply.lex as lex
import ply.yacc as yacc
import math
#Tokens definition
tokens=('NAME','NUMBER', 'PLUS','MINUS', 'TIMES',
         'DIVIDE', 'EQUALS','LPAREN', 'RPAREN','SIN','COS','TAN','SQRT')
#Dictionary of names
names={}


#Regular Expressions reganding tokens
t_PLUS  =   r'\+'
t_MINUS  =   r'\-'
t_TIMES  =   r'\*'
t_DIVIDE  =   r'\/'
t_EQUALS  =   r'\='
t_LPAREN  =   r'\('
t_RPAREN  =   r'\)'
t_NAME  =   r'[a-zA-Z_]+[a-zA-Z0-9]*'
t_ignore  = ' \t'



def t_NUMBER(t):
    r'\d+'
    try:
        t.value=int(t.value)
    except ValueError:
        print('Integer is wrong %d', t.value)
    return t
def t_error(t):
    print('Illegal character %s'% t.value[0])
    t.lexer.skip(1)

def t_SIN(t):
    r'SIN|sin'
    return t

def t_COS(t):
    r'COS|cos'
    return t

def t_TAN(t):
    r'TAN|tan'
    return t

def t_SQRT(t):
    r'SQRT|sqrt'
    return t

precedence = (
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE'),
    ('right','UMINUS'),
)

#Define grammar rules
def p_statement_assign(t):
    'statement : NAME EQUALS expression'
    names[t[1]]=t[3]
    #print(t[1],t[2],t[3])

def p_statement_expr(t):
    'statement : expression'
    #print(t[0])

def p_expression_sum(t):
    'expression :   expression PLUS expression'
    t[0]=t[1]+t[3]
    print(t[0])

def p_expression_diff(t):
    'expression :   expression MINUS expression'
    t[0]=t[1]-t[3]
    print (t[0])

def p_expression_prod(t):
    'expression :   expression TIMES expression'
    t[0]=t[1]*t[3]
    print(t[0])
    
def p_expression_div(t):
    'expression :   expression DIVIDE expression'
    try:
        t[0]=t[1]/t[3]
        print(t[0])
    except ZeroDivisionError:
        print("Division by zero")

def p_expression_sin(t):
    'expression :   SIN LPAREN expression RPAREN'
    t[0]=math.sin(t[3])
    print(t[0])

def p_expression_cos(t):
    'expression :   COS LPAREN expression RPAREN'
    t[0]=math.cos(t[3])
    print(t[0])

def p_expression_tan(t):
    'expression :   TAN LPAREN expression RPAREN'
    t[0]=math.tan(t[3])
    print(t[0])

def p_expression_sqrt(t):
    'expression :   SQRT LPAREN expression RPAREN'
    t[0]=math.sqrt(t[3])
    print(t[0])

def p_factor_neg(t):
    'expression :   MINUS expression %prec UMINUS'
    t[0]=-t[2]

def p_expression_number(t):
    'expression : NUMBER'
    t[0]=t[1]
    #print(t[1])
     
def p_expression_name(t):
    'expression :   NAME'
    try:
        t[0]=names[t[1]]
    except LookupError:
        print("Undefined name '%s'"%t[1])
        t[0]=0

def p_error(t):
    print("Syntax error at '%s'" %t.value)
#Lexical Analysis
#Step 1: Build the lexer
lexer = lex.lex()
#s=input('cinves_calc >')
#lexer.input(s)

# Tokenize
#while True:
 #   tok = lexer.token()
 #   if not tok: 
 #       break      # No more input
 #   print(tok)


parser= yacc.yacc()
try:
    while True:
        try:
            s = input('calc > ')
        except EOFError:
            break
        if not s: continue
        parser.parse(s)
except KeyboardInterrupt:
    print("\nBye")
   #print(result)
   #print(names)

