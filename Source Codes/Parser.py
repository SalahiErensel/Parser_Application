from Definer import is_integer

#Globals table that stores token functions

globals = {'input_token_index': -1, 'next_token': '$', 'input_tokens': [], 'error': False}

class Node:

    def __init__(self, symbol='', left_child=None, right_child=None):

        self.left_child = left_child

        self.right_child = right_child

        self.symbol = symbol

#Function of G ---> E
   
    def G(self):
   
        lex()
   
        print("G ---> E")
   
        tree = self.E()
   
        if globals['next_token'] == '$' and not globals['error']:
   
            print("\nSuccess.")
   
            return tree
   
        else:
   
            print("Failure: Unconsumed input: " + self.unconsumed_input())
   
            return None

    # Function of E ---> T R
    
    def E(self):
    
        if globals['error']:
    
            return None
    
        print("E ---> T R")
    
        temp = self.T()
    
        return self.R(temp)

    # Function of R ---> + T R | - T R | e
    
    def R(self, tree):
    
        if globals['error']:
    
            return None
    
        if globals['next_token'] == '+':
    
            print("R ---> + T R")
    
            lex()
    
            temp1 = self.T()
    
            temp2 = self.R(temp1)
    
            x = Node('+', tree, temp2)
    
            return x
    
        elif globals['next_token'] == '-':
    
            print("R ---> - T R")
    
            lex()
    
            temp1 = self.T()
    
            temp2 = self.R(temp1)
    
            x = Node('-', tree, temp2)
    
            return x
    
        else:
    
            print("R ---> e")
    
            return tree

    # Function of T -> F S
    
    def T(self):
        
        if globals['error']:
        
            return None
        
        print("T ---> F S")
        
        temp = self.F()
        
        return self.S(temp)

    # Function of S -> * F S | / F S | e
    
    def S(self, tree):
    
        if globals['error']:
    
            return None
    
        if globals['next_token'] == '*':
    
            print("S ---> * F S")
    
            lex()
    
            temp1 = self.F()
    
            temp2 = self.S(temp1)
    
            x = Node("*", tree, temp2)
    
            return x
    
        elif globals['next_token'] == '/':
    
            print("S -> / F S")
    
            lex()
    
            temp1 = self.F()
    
            temp2 = self.S(temp1)
    
            x = Node("/", tree, temp2)
    
            return x
    
        else:
    
            print("S ---> e")
    
            return tree

    #Function of F ---> ( E ) | N 
    
    def F(self):
    
        if globals['error']:
    
            return None
    
        if globals['next_token'] == '(':
    
            print("F ---> ( E )")
    
            lex()
    
            temp = self.E()
           
            if globals['next_token'] == ')':
           
                lex()
           
                return temp
           
            else:
           
                globals['error'] = True
           
                print("error: unexpected token " + globals['next_token'])
           
                return None
       
        elif is_integer(globals['next_token']):
       
            print("F ---> N")
       
            return self.N()
       
        else:
       
            globals['error'] = True
       
            print("error: unexpected token " + globals['next_token'])
       
            return None


    # Function of N ---> 0 | 1 | 2 | 3 | 4 |5 | 6 | 7 | 8 | 9
    
    def N(self):
    
        prev_token = globals['next_token']
    
        if globals['error']:
    
            return None
    
        if is_integer(globals['next_token']):
    
            print("N ---> " + globals['next_token'])
    
            lex()
    
            x = Node(prev_token)
    
            return x
    
        else:
    
            globals['error'] = True
    
            print("error: unexpected token " + globals['next_token'])
    
            return None

    
    def unconsumed_input(self):
       
        pass

def unconsumed_input():

    return globals['input_tokens'][globals['input_token_index']:]

def lex():

    globals['input_token_index'] = globals['input_token_index'] + 1

    globals['next_token'] = globals['input_tokens'][globals['input_token_index']]

    if globals['next_token'].isspace():

        lex()

def initialize_parse(input_tokens):

    globals['input_tokens'] = input_tokens

#Function for parse tree

def print_tree(tree):

    if tree is None:

        return None

    else:

        print_tree(tree.left_child)

        print_tree(tree.right_child)

        print(tree.symbol)