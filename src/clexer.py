import re

# Token types
TOKEN_TYPES = {
    'ALTER': r'ALTER',
    'COMMA': r',',
    'BOOLEAN': r'BOOLEAN',
    'BOOLEAN_VALUE': r'(?:TRUE|FALSE)',
    'CHAR': r'CHAR',
    'CONSTRAINT': r'CONSTRAINT',
    'CREATE': r'CREATE',
    'TABLE': r'TABLE',
    'DATE': r'DATE',
    'DEFAULT': r'DEFAULT',
    'FLOAT': r'FLOAT',
    'FOREIGN': r'FOREIGN',
    'INTEGER': r'INTEGER',
    'DECIMAL': r'[0-9]+\.[0-9]+',
    'KEY': r'KEY',
    'LPAREN': r'\(',
    'NOT': r'NOT',
    'NULL': r'NULL',
    'INT': r'INT',
    'PRIMARY': r'PRIMARY',
    'FOREIGN': r'FOREIGN',
    'REFERENCES': r'REFERENCES',
    'RPAREN': r'\)',
    'SEMICOLON': r';',
    'IDENTIFIER': r'[a-zA-Z_][a-zA-Z0-9_]*',
    'VALUE': r'\d+',
    'UNIQUE': r'UNIQUE',
    'VARCHAR': r'VARCHAR',
    'WHITESPACE': r'\s+',
}


#'NUMBER': r'[0-9]+',

def lexer1(input_string):

    TOKEN_REGEX = '|'.join('(?P<%s>%s)' % pair for pair in TOKEN_TYPES.items())
    """
    Lexical analyzer for SQL CREATE TABLE statements.
    """
    tokens = []
    for match in re.finditer(TOKEN_REGEX, input_string):
        token_type = match.lastgroup
        token_value = match.group(token_type)
        if token_type != 'WHITESPACE':
            tokens.append((token_type, token_value))
    return tokens

def lexer2(input_string):

    tokens = []
    while input_string:
        match = None
        for token, pattern in TOKEN_TYPES.items():
            regex = re.compile(pattern)
            match = regex.match(input_string)
            if match:
                value = match.group(0)
                if token != 'WHITESPACE':
                    tokens.append((token, value))
                input_string = input_string[len(value):]
                break
        if not match:
            raise SyntaxError(f"Unexpected character: {input_string[0]}")
    return tokens

