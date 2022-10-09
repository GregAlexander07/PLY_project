import ply.lex as lex

tokens = ['ID', 'NUM', 'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE',
          'BECOMES', 'EQ', 'NE', 'LT', 'GT', 'LE', 'GE',
          'PLUS', 'MINUS', 'STAR', 'SLASH', 'PCT', 'COMMA',
          'SEMI', 'COLON', 'ARROW', 'COMMENT', 'WHITESPACE']

reserved = {"def": "DEF", "if": "IF", "var": "VAR",
            "Int": "INT","else": "ELSE", }

# t_OPERATOR = r"(\*|\/|\=|\!=|\<=|\>=|\<|\>|\&)"
# Define tokens, will be imported into the parser file
tokens = tokens + list(reserved.values())

t_PLUS = r'\+'
t_MINUS = r'-'
t_STAR = r'\*'
t_SLASH = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_BECOMES = r'='
t_EQ = r'=='
t_COMMA = r','
t_COMMENT = r'//(.*)\n'
t_LBRACE = r'{'
t_RBRACE = r'}'
t_NE = r'!='
t_LT = r'<'
t_GT = r'>'
t_LE = r'<='
t_GE = r'>='
t_PCT = r'%'
t_SEMI = r';'
t_COLON = r':'
t_ARROW = r'=>'

# Define REGEX rules
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, "ID")
    return t

def t_NUM(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

t_ignore = " \t"


# Creat lex object
lexer = lex.lex()

# data = ''''''
# Give the lexer some input
# lexer.input(data)

# Tokenize
# while True:
#    tok = lexer.token()
#    if not tok:
#        break  # No more input
#   print(tok.type, tok.value, tok.lineno, tok.lexpos)
