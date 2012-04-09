#!/usr/bin/python -tt

import sys
import re

class LexerException(Exception):
    pass

patterns = [
    (r'(PRINT)', 'PRINT_KW'),
    (r'(LET)', 'LET_KW'),
    (r'(REPEAT)', 'REPEAT_KW'),
    (r'(UNTIL)', 'UNTIL_KW'),
    (r'([a-zA-Z]\w*)', 'IDENTIFIER'),
    (r'(<|>|>=|<=|==|!=)', 'RELOP'),
    (r'(\d+)', 'NUMBER'),
    (r'"(.*?)"', 'STRING'),
    (r"'(.*?)'", 'STRING'),
    (r'(\+)', '+'),
    (r'(-)', '-'),
    (r'(\*)', '*'),
    (r'(/)', '/'),
    (r'(=)', '='),
    (r'(\()', '('),
    (r'(\))', ')'),
    (r'(:)', ':'),
    (r'(;)', ';'),
    (r'\s+', None)
]

def tokenize(input):
    lineno = 0

    for line in input:
        lineno += 1;
        pos = 0

        while pos < len(line):
            matched = False
            for pattern, token in patterns:
                regexp = re.compile(pattern)
                match = regexp.match(line, pos)
                if match:
                    matched = True
                    pos = match.end()
                    if token is not None:
                        yield (token, match.group(1))
    
            if not matched:
                raise LexerException('Unable to tokenize at line', lineno)

if __name__ == '__main__':
    for token in tokenize(file(sys.argv[1])):
        print token

