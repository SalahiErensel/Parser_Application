from file_read import File

from Parser import Node, initialize_parse, print_tree, globals

from Definer import *

introduction()

number_chosen = 0

print("\n")

#Loop for displaying menu

while True:
    
    print("Please choose a number to continue:\n")
    
    print("1. Enter the File Name. \n")
    
    print("2. Exit. \n")
    
    number_chosen = int(input("Enter the number: "))
    
    #If choice 1 is chosen, the file name that wanted to be executed should be entered and the application will execute a tree using the file stores.
   
    if number_chosen == 1:
    
        file_name = input("Enter the file name you want to execute : ")
        
        inputFile = File(file_name + ".txt")
        
        input_tokens = inputFile.read_from_file()
        
        initialize_parse(input_tokens)
        
        tree = Node().G()
        
        if not globals['error']:
        
            print_tree(tree)
        
        else:
        
            print("Unsuccessful parsing!!")
        
        print("\n")
    
    #If choice 2 is chosen,program will stop.
    
    elif number_chosen == 2:
    
        print("The system has been logged out.")
    
        end_the_program()
    
    #If anything entered rather than 1 or 2,Program will return invalid input.
    
    else:
    
        print("Invalid input!! Try again later.\n")