from Tokens import reserved_words, operators

def introduction():
    
    print("\t-------->Parser and Lexical Application made by Hasan and Salahi!!<----------")

#Checking if inputtoken is identifier or not

#If first character is alphabet or _ the token is identifier but not if starts with reversed words or numbers

def is_identifier(input_token):

    if reserved_words.count(input_token) > 0:

        return False

    elif input_token[0].isalpha() or input_token[0] == "_":

        return True

    else:

        return False

#Checking if input_token is reversed word which can be for,while,if,else

def is_reserved_word(input_token):

    return bool(reserved_words.count(input_token))

#Checking if input_token is operator which can be &,&&,|,||

def is_operator(input_token):

    return bool(operators.count(input_token))

#Checking if number is integer

def is_integer(num):

    try:

        float(num)

    except ValueError:

        return False

    else:

        return float(num).is_integer()

#Checking if number is float

def is_float(num):

    try:

        int_num = int(num)

    except ValueError:

        try:

            float_num = float(num)

        except ValueError:

            return False

        else:

            return True

    else:

        return False

#Exitting from program

def end_the_program():

    exit()