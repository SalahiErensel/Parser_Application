from Definer import *

from Tokens import reserved_words, Tokenize

#Creating a symbol table with array

symbol_table = []

symbol_table.extend(reserved_words)


def lexical_results(input_token, value=None):

    return value

#Adding to symbol table array

def add_to_symbol_table(identifier):

    if symbol_table.count(identifier):

        return symbol_table.index(identifier)

    else:

        symbol_table.append(identifier)

        return symbol_table.index(identifier)

#Printing symbol table

def print_symbol_table():

    return "Symbol Table: " + str(symbol_table)

#Lex function 

def _lex(input_token):

    if is_operator(input_token):

        return lexical_results(input_token)

    elif is_identifier(input_token):

        index = add_to_symbol_table(input_token)

        return lexical_results(input_token="id", value=index)

    elif is_reserved_word(input_token):

        return lexical_results(input_token)

    elif is_integer(input_token):

        x = int(input_token)

        return lexical_results(input_token="int", value=x)

    elif is_float(input_token):

        x = float(input_token)

        return lexical_results(input_token="float", value=x)

    else:

        return lexical_results(input_token="err", value=input_token)