from enum import Enum

#Creating reversed_words array to store reversed words.

reserved_words = ["for", "while", "if", "else"]

#Creating operators array to store operators allowed.

operators = ["|", "||", "&", "&&"]

#Creating tokens with Tokenize class with use of Enum directory and defining each token in it.

class Tokenize(Enum):

    FOR = "for"

    WHILE = "while"

    IF = "if"

    ELSE = "else"

    INTEGER = "int"

    FLOAT = "float"

    BITWISE_OR = "|"

    LOGICAL_OR = "||"

    BITWISE_AND = "&"

    LOGICAL_AND = "&&"

    ID = "id"

    ERROR = "err"
