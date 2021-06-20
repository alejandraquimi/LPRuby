import ply.lex as lex

tokens = (
    'NUMBER',
    'FLOAT',
    'STRING',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'LCOR',
    'RCOR',
    'MAYORQUE',
    'MENORQUE',
    'NUMERAL',
    'IGUAL',
    'COMMA',
    'PUNTO',
    'FLECHA'
    'ID',
 )
# Reglas de expresión regular para tokens simples
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_MOD = r'%'
t_LCOR = r'\['
t_RCOR = r'\]'
t_MAYORQUE = r'>'
t_MENORQUE = r'<'
t_EQUAL = r'='
t_COMMA = r','
t_PUNTO = r'\.'
t_FLECHA = r'=>'
t_NUMERAL = r'\#'
