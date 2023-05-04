line = []
lex = ""
lex_name = " "
statement = []
stmt_counter = 1
found_numbers = ""
out_file = None

import sys
from functools import partial

def get_token(token):
    # line
    global lex
    global lex_name
    global statement
    global stmt_counter

    # print("in get_token")
    check_white_space(token, add_to_statement)
    if token == ';':
        process_statement(statement)
        out_file.write("\n")
        statement = []
        stmt_counter = increment_statements(stmt_counter)
        file_updater = write_to_file(None)
        

def process_statement(statement):
    global out_file
    for x in statement:
        file_updater = write_to_file(x)
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print(x)
        file_updater(lex, lex_name, out_file, 0)
        # out_file.write(x)

def write_to_file(token):
    global lex_name
    if (
        #is_digit(token)
        is_literal(token)
        or is_equality(token)
        or is_arithmetic(token)
    ):
        return update
    elif token is None:
        return statement_prompt

# function definition which calls another function definition
# with at least one function definition
def check_white_space(token, fn):
    if token != ' ' and token != '\n' and token != '\t':
        fn(token)

def add_to_statement(token):
    statement.append(token)

#pure function
def increment_statements(i):
    return i+1

# recursion
def read_next_line(file, outfile, thisline):
    lineLength = len(thisline)
    for i in range(lineLength):
        get_token(thisline[i])

    # outfile.writelines(thisline)

    nextLine = file.readline()
    if not nextLine:
        return 0
    else:
        read_next_line(file, outfile, nextLine)




def update(curr_token, lex_type, out_file, current_count):

    global lex
    if is_vowel(lex_type[0]) == True:
        out_file.write(
            "Lexeme " + str(current_count) + " is " + curr_token + " and is an " + lex_type + "\n"
        )
    else:
        out_file.write(
            "Lexeme " + str(current_count) + " is " + curr_token + " and is a " + lex_type + "\n"
        )

    if lex_name == "SEMI_COLON":
        out_file.write("________________________________\n")


def statement_prompt(out_file, start):
    out_file.write("Statement " + str(start) + "\n")


def lex_error(out_file, token):
    out_file.write("==> " + str(token) + "\nLexical error: not a lexeme\n\n")


def is_vowel(c):
    found = False

    to_check = c.lower()

    if (
        to_check == "a"
        or to_check == "e"
        or to_check == "i"
        or to_check == "o"
        or to_check == "u"
    ):

        found = True

    return found


def is_digit(c):
    #global lex
    found = False

    if (
        c == "0"
        or c == "1"
        or c == "2"
        or c == "3"
        or c == "4"
        or c == "5"
        or c == "6"
        or c == "7"
        or c == "8"
        or c == "9"
    ):

        found = True
     #   lex = c

    return found


def is_arithmetic(token_ptr):
    found = False                                                               
    global lex_name                                                             
    global lex                                                                  
    
    arithmetic = ['+', '-', '*', '/', '^']

    print(token_ptr)                                                                            
    #global line                                                                 
    result = list(filter(lambda op: True if op == token_ptr else False, arithmetic))                                                                            
    print("in is_arithmetic")
    print(result)                                                   
    print(len(result))                                                              
    if len(result) > 0:                                                         
        found = True                                                            
                                                                                
        if token_ptr == '+':                                                    
            lex = "+"                                                           
            lex_name = "ADD_OP"                                                 
                                                                                
        elif token_ptr == '-' :                                                 
            lex = "-"                                                           
            lex_name = "SUB_OP"                                                 
                                                                                
        elif token_ptr == '*':                                                  
            lex = "*"                                                           
            lex_name = "MULT_OP"                                                
                                                                                
        elif token_ptr == '/':                                                  
            lex = "/"                                                           
            lex_name = "DIV_OP"                                                 
                                                                                
                                                                                
        elif token_ptr  == '^':                                                 
            lex = "^"                                                           
            lex_name = "EXPON_OP"                                               
    
        print(result)                                                                            
    print(lex_name)
    print("in is_ARTH")                                                                            
    return found                                                                


def concat(found_numbers, c):                                                   
    #global found_numbers                                                       
                                                                                
    found_numbers = found_numbers + c                                           
    return found_numbers                                                        



def check_for_eq(token_ptr):                                                    
    if token_ptr == '=':                                                        
        return True                                                             
    else:                                                                       
        return False                                                            


def is_literal(token_ptr):
    found = False                                                               
    global lex_name                                                             
    global lex                                                                  
    global statement                                                                            
    #global found_numbers                                                       
                                                                                
    print("in is_literal")                                                      
    print(line)                                                                 
                                                                                
    print(token_ptr)                                                            
    print(is_digit(token_ptr))                                                  
                                                                                
    nums = []
    #token_index = statement.index(token_ptr)
    if is_digit(token_ptr) == True:
        token_index = statement.index(token_ptr)                                             
        #token_index = statement.index(token_ptr)
        found = True                                                            
        #result = reduce(concat, token_ptr, "")                                           
        lex_name = "INT_LITERAL"                                                
        
        index = statement.index(token_ptr)

        while is_digit(statement[index]) == True:
            
            if index > 0 and is_digit(statement[index -1]):

                nums.append(statement.pop(index)) 
            
            else:
                nums.append(statement[index])
                index+=1
            #statement.pop(index)
            #print(statement[index])
            #index+=1
            #statement.pop(index)
            #also remove them from the list
        result = reduce(concat, nums, "")
        
        lex = result                                                     
        statement[token_index] = result                                                                        
       
       #while is_digit() == True:                                              
            #functools.reduce(concat, line[1], 0)                               
        #    line+=1                                                            
                                                                                
     #   print(found_numbers)                                                   
    print(found)                                                                
    print(lex_name)                                                             
    print(lex_name[0])                                                          
    print(token_ptr)                                                            

    if token_ptr == "(":
        lex = "("
        lex_name = "LEFT_PAREN"

        found = True

    elif token_ptr == ")":
        lex = ")"
        lex_name = "RIGHT_PAREN"

        found = True

    elif token_ptr == ";":
        lex = ";"
        lex_name = "SEMI_COLON"

        found = True

    return found


def is_equality(token_ptr):
    global statement
    global lex_name                                                             
    global lex                                                                  
    found = False                                                               
                                                                                
                                                                                
    two = []                                                                    
    

    print("in is_equality")
    print(statement)
    #token_index = statement.index(token_ptr)
    #REMOVE IT 
    if token_ptr == "=":                                                        
        token_index = statement.index(token_ptr)                                                                          
        if check_for_eq(statement[token_index + 1]) == True:                                     
            two = ['=', '=']                                                    
            concat_with_found_numbers = partial(concat, found_numbers)
            result = list(map(concat_with_found_numbers, two))                                     
                                                                                
            print(result)                                                       
            result[0] = result[0] + result[1]                                   
            lex = result[0]                                                     
                                                                                
            lex_name = "NOT_EQUALS_OP"                                          
            statement[token_index] = result[0]                                  
                                                                                
            lex_name = "EQUALS_OP"
            statement.remove('=')
        else:                                                                   
            lex = "="                                                           
            lex_name = "ASSIGN_OP"                                              
                                                                                
        found = True                                                            
                                                                                
    elif token_ptr == "<":                                                      
        token_index = statement.index(token_ptr)                                                                        
        if check_for_eq(statement[token_index + 1]) == True:                                     
            two = ['<', '='] 
            concat_with_found_numbers = partial(concat, found_numbers)
            result = list(map(concat_with_found_numbers, two))                                     
                                                                                
            print(result)                                                       
                                                                                
            result[0] = result[0] + result[1]                                   
            lex = result[0]                                                     
                                                                                
            lex_name = "NOT_EQUALS_OP"                                          
            statement[token_index] = result[0]                                  
                                                                                
            lex_name = "LESS_THEN_OR_EQUAL_OP"
            statement.remove('=')
        else:                                                                   
            lex = "<"                                                           
            lex_name = "LESS_THEN_OP"                                           
                                                                                
        found = True                                                            
                                                                                
    elif token_ptr == ">":
        token_index = statement.index(token_ptr)                                                          
        if check_for_eq(statement[token_index + 1]) == True:                                     
            two = ['>', '=']
            concat_with_found_numbers = partial(concat, found_numbers)
            result = list(map(concat_with_found_numbers, two))                                     
            print(result)                                                       
                                                                                
            result[0] = result[0] + result[1]                                   
            lex = result[0]                                                     
                                                                                
            lex_name = "NOT_EQUALS_OP"                                          
            statement[token_index] = result[0]                                  
                                                                                
            lex_name = "GREATER_THEN_OR_EQUAL_OP"                               
            statement.remove('=')                                                                    
        else:                                                                   
            lex = ">"                                                           
            lex_name = "GREATER_THEN_OP"                                        
                                                                                
        found = True                                                            
                                                                                
    elif token_ptr == "!":
        token_index = statement.index(token_ptr)                                                      
        if check_for_eq(statement[token_index + 1]) == True:                                     
            two = ['!', '=']           
            concat_with_found_numbers = partial(concat, found_numbers)
            result = list(map(concat_with_found_numbers, two))                                     
                                                                                
            print("--------------------------------------")
            print(result)
                                                                   
            result[0] = result[0] + result[1]                                                                    
            lex = result[0]                                                     
                                                                                
            lex_name = "NOT_EQUALS_OP"
            statement[token_index] = result[0]
            print(statement[token_index])
            print(statement[token_index -1])
            print(statement[token_index +1])
            statement.remove('=')
            
        else:                                                                   
            lex = "!"                                                           
            lex_name = "NOT_OP"                                                 
                                                                                
        found = True                                                            
                                                                                
    return found                                                                


def main():
    input_line = None
    in_file = None
    global out_file
    if len(sys.argv) != 3:                                                      
        print("Usage: tokenizer inputFile outputFile")                          
        sys.exit(1)                                                             
                                                                                
    try:                                                                        
        in_file = open(sys.argv[1], "r")                                        
    except IOError:                                                             
        sys.stderr.write("ERROR: could not open %s for reading\n" % sys.argv[1])
        sys.exit(1)                                                             
                                                                                
    try:                                                                        
        out_file = open(sys.argv[2], "w")                                       
    except IOError:                                                             
        sys.stderr.write("ERROR: could not open %s for writing\n" % sys.argv[2])


    start = 0
    count = 0

    read_next_line(in_file, out_file, in_file.readline())

    in_file.close()
    out_file.close()
    return 0


if __name__ == "__main__":
    main()


