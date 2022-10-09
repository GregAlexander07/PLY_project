import lexer
import ply.yacc as yacc
import logging

# logger set up for debugging purposes
logging.basicConfig(
    level=logging.DEBUG,
    filename="parselog.txt",
    filemode="w",
    format="%(filename)0s:%(lineno)4d:%(message)s"
)

log = logging.getLogger()

tokens = lexer.tokens

precedence = (('left', 'COMMA'),
              ('left', 'PLUS', 'MINUS'),
              ('left', 'STAR', 'SLASH'),
              )

# Identify starting line
start = 'defdefs'


# defdefs -> defdef defdefs
def p_defdefs_defdef_defdefs(p):
    'defdefs : defdef defdefs'
    pass


# defdefs -> defdef
def p_defdefs_defdef(p):
    'defdefs : defdef'
    pass


# defdef -> DEF ID LPAREN parmsopt RPAREN COLON type BECOMES LBRACE vardefsopt defdefsopt expras RBRACE
def p_defdef_id(p):
    'defdef : DEF ID LPAREN parmsopt RPAREN COLON type BECOMES LBRACE vardefsopt defdefsopt expras RBRACE'
    pass


# parmsopt -> parms
def p_parmsopt_parms(p):
    'parmsopt : parms'
    pass


# parmsopt ->
def p_parmsopt(p):
    'parmsopt :'
    pass


# parms -> vardef COMMA parms
def p_parms_vardef_comma_parms(p):
    'parms : vardef COMMA parms'
    pass


# parms -> vardef
def p_parms_vardef(p):
    'parms : vardef'


# vardef -> ID COLON type
def p_vardef_id_colon_type(p):
    'vardef : ID COLON type'
    pass


# type -> INT
def p_type_int(p):
    'type : INT'
    pass


# type -> LPAREN typesopt RPAREN ARROW type
def p_type_laparen_typesopt_rparen_arrow_type(p):
    'type : LPAREN typesopt RPAREN ARROW type'
    pass


# typesopt -> types
def p_typesopt_types(p):
    'typesopt : types'
    pass


# typesopt ->
def p_typesopt(p):
    'typesopt :'
    pass


# types -> type COMMA types
def p_types_type_COMMA_types(p):
    'types : type COMMA types'
    pass


# types -> type
def p_types_type(p):
    'types : type'
    pass


# vardefsopt ->  VAR vardef SEMI vardefsopt
def p_vardefsopt_var_vardef_semi_vardefsopt(p):
    'vardefsopt : VAR vardef SEMI vardefsopt'
    pass


# vardefsopt ->
def p_vardefsopt(p):
    'vardefsopt :'
    pass


# defdefsopt -> defdefs
def p_defdefsopt_defdef(p):
    'defdefsopt : defdefs'
    pass


# defdefsopt ->
def p_defdefsopt(p):
    'defdefsopt :'
    pass


# expras -> expra SEMI expras
def p_expras_expra_semi_expras(p):
    'expras : expra SEMI expras'
    pass


# expras -> expra
def p_expras_expra(p):
    'expras : expra'
    pass


# expra -> ID BECOMES expr
def p_expra_id_becomes_expr(p):
    'expra : ID BECOMES expr'
    pass


# expra -> expr
def p_expra_expr(p):
    'expra : expr'
    pass


# expr -> IF LPAREN test RPAREN LBRACE expras RBRACE ELSE LBRACE expras RBRACE
def p_expr_if_lparen_test(p):
    'expr : IF LPAREN test RPAREN LBRACE expras RBRACE ELSE LBRACE expras RBRACE'
    pass


# expr -> term
def p_expr_term(p):
    'expr : term'
    pass


# expr -> expr  PLUS term
def p_expr_plus_term(p):
    'expr : expr PLUS term'


# expr -> expr MINUS term
def p_expr_minus_term(p):
    'expr : expr MINUS term'
    pass


# term -> factor
def p_term_factor(p):
    'term : factor'
    pass


# term -> term STAR factor
def p_term_star(p):
    'term : term STAR factor'
    pass


# term -> term SLASH factor
def p_term_slash(p):
    'term : term SLASH factor'
    pass


# term -> term PCT factor
def p_term_pct(p):
    'term : term PCT factor'
    pass


# factor -> ID
def p_factor_id(p):
    'factor : ID'
    pass


# factor -> NUM
def p_factor_num(p):
    'factor : NUM'
    pass


# factor -> LPAREN expr RPAREN
def p_factor_lparen_expr_rparen(p):
    'factor : LPAREN expr RPAREN'
    pass


# factor -> factor LPAREN argsopt RPAREN
def p_factor_factor_lparen_argsopt_rparen(p):
    'factor : factor LPAREN argsopt RPAREN'
    pass


# test -> expr NE expr
def p_test_expr_ne_expr(p):
    'test : expr NE expr'
    pass


# test -> expr LT expr
def p_test_expr_lt_expr(p):
    'test : expr LT expr'
    pass


# test -> expr LE expr
def p_test_expr_le_expr(p):
    'test : expr LE expr'
    pass


# test -> expr GE expr
def p_test_expr_ge_expr(p):
    'test : expr GE expr'
    pass


# test -> expr GT expr
def p_test_expr_gt_expr(p):
    'test : expr GT expr'
    pass


# test -> expr EQ expr
def p_test_expr_eq_expr(p):
    'test : expr EQ expr'
    pass


# argsopt -> args
def p_argsopt_args(p):
    'argsopt : args'
    pass


# argsopt - >
def p_argspot(p):
    'argsopt :'
    pass


# args -> expr COMMA args
def p_expr_comma_args(p):
    'args : expr COMMA args'
    pass


# args -> expr
def p_args_expr(p):
    'args : expr'
    pass


def p_error(p):
    if not p:
        print("EOF!")
        return
    while True:
        tok = parser.token()
        if not tok or tok.type == 'SEMI':
            break
    parser.restart()

#Create parser or yacc object
parser = yacc.yacc(debug=True)

# result = parser.parse("def f(a:Int, b:Int):Int = { var c:Int; def g(a:Int, b:(Int)=>Int):Int = { b(a)} def h(c:Int):Int = { def g():Int = { c-b}")
#def f(a:Int, b:Int):Int = { var c:Int;def g(a:Int, b:(Int)=>Int):Int = { b(a)}def h(c:Int):Int = {=>def g():Int = { c-b}g() }c = a+b;g(c,h)}
# Enter Input to parse
while True:
    try:
        test = input('Enter Input:  ')
    except EOFError:
        break
    if not test: continue
    result = parser.parse(test, debug=log)
    print(result)
