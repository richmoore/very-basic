#!/usr/bin/python -tt

import pprint

symbols = {}

#
# Expressions
#

def factor(node):
    self, rest = node[0], node[1:]

    if rest[0][0] == '(':
        return expression(rest[1])
    elif rest[0][0] == 'NUMBER':
        return int(rest[0][1])
    elif rest[0][0] == 'STRING':
        return rest[0][1]
    elif rest[0][0] == 'IDENTIFIER':
        return symbols[rest[0][1]]

def term(node):
    self, rest = node[0], node[1:]

    if len(rest) == 3:
        if rest[1][0] == '*':
            left = term(rest[0])
            right = factor(rest[2])
            return left * right
        elif rest[1][0] == '/':
            left = term(rest[0])
            right = factor(rest[2])
            return left / right
    else:
        return factor(rest[0])

def expression(node):
    self, rest = node[0], node[1:]

    if len(rest) == 3:
        if rest[1][0] == '+':
            left = expression(rest[0])
            right = term(rest[2])
            return left + right
        elif rest[1][0] == '-':
            left = expression(rest[0])
            right = term(rest[2])
            return left - right
    else:
        return term(rest[0])

#
# Conditional expressions
#
def boolean_expression(node):
    self, rest = node[0], node[1:]

    left = expression(rest[0])
    right = expression(rest[2])

    op = rest[1][1]
    if op == '==':
        return left == right
    elif op == '<':
        return left < right
    elif op == '>':
        return left > right
    elif op == '<=':
        return left <= right
    elif op == '>=':
        return left >= right
    elif op == '!=':
        return left != right

#
# Statements
#

def print_statement(node):
    self, rest = node[0], node[1:]
    prnt, expr = rest

    value = expression(expr)
    print value

def repeat_statement(node):
    self, rest = node[0], node[1:]

    repeat, stmts, until, condition = rest

    while True:
        statements(stmts)
        if boolean_expression(condition):
            break

def let_statement(node):
    self, rest = node[0], node[1:]
    let, identifier, equal, expr = rest

    value = expression(expr)
    symbols[identifier[1]] = value

def statement(node):
    self, rest = node[0], node[1:]

    if rest[0][0] == 'PRINT_KW':
        print_statement(node)
    elif rest[0][0] == 'REPEAT_KW':
        repeat_statement(node)
    elif rest[0][0] == 'LET_KW':
        let_statement(node)

def statements(node):
    self, rest = node[0], node[1:]

    for n in rest:
        if n[0] == 'statement':
            statement(n)
        elif n[0] == 'statements':
            statements(n)

#
# Main
#

def run(tree):
    #pprint.pprint(tree)
    statements(tree)
