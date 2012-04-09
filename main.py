#!/usr/bin/python -tt

from lexer import tokenize
from parser import Parser
from runtime import run

def print_tree(tree, terminals, indent=0):
    """Print a parse tree to stdout."""
    prefix = "    "*indent
    if tree[0] in terminals:
        print prefix + repr(tree)
    else:
        print prefix + unicode(tree[0])
        for x in tree[1:]:
            print_tree(x, terminals, indent+1)

def main(filename):
    input = open(filename)

    parser = Parser()

    try:
        tree = parser.parse(tokenize(input))
        #print_tree(tree, parser.terminals)

        run(tree)

    except parser.ParseErrors, e:
        for token, expected in e.errors:
            print 'Found', token, 'when', expected, 'was expected'

if __name__ == '__main__':
    import sys
    filename = sys.argv[1]
    main(filename)
