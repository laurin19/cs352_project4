line = None
lex = None
lex_name = None
found_numbers = ""

import sys

"""
def get_line(in_file, out_file, input_line):
    start = 0
    count = 0

    line = input_line

    for input_line in in_file:
        #using .strip() to remove whitespace from the line
        global line = input_line.strip()

            while line != '\0':
                if count == 0 and not line[pointer].isspace():
                    statement_prompt(out_file, start)
                    start++;
                    
                if not line[pointer].isspace():
                    get_token(line)

                if lex_name == "ERROR" and not line[pointer].isspace():
                    lex_error(out_file, lex)

                elif not line[pointer].isspace() and lex_name != "INT_LITERAL":
                    update(lex, lex_name, out_file, count)
                    count+=1
                elif not line[pointer].isspace() and lex_name == "INT_LITERAL":
                    update(found_numbers, lex_name, out_file, count)
                    count+=1
                    found_numbers = ""

                if lex_name == "SEMI_COLON":
                    count = 0;

                line++
                #close files
    return 0

"""

def get_token(token):
    line+=1

    #if line[].isspace():
     #  line+=1

def print_line(out_file):
    out_file.write(line);
    

def update(curr_token, lex_type, out_file, current_count):
    if is_vowel(lex_type[0]) == True:
        out_file.write("Lexeme", current_count, "is", curr_token, "and is an",
                       lex_type, "\n")
    else:
        out_file.write("Lexeme", current_count, "is", curr_token, "and is a",
                       lex_type, "\n")

    if lex_name == "SEMI_COLON":
        out_file.write("________________________________\n")

def statement_prompt(out_file, start):
    out_file.write("Statement", start, "\n")

def lex_error(out_file, token):
    out_file.write("==>", token, "\nLexical error: not a lexeme\n\n")

def is_vowel(c):
    found = False

    to_check = c.lower()

    if to_check == 'a' or to_check == 'e' or to_check == 'i' or to_check == 'o'or to_check == 'u':
        
            found = True

    return found

def is_digit(c):
    found = False
    
    if c == '0' or c == '1' or c == '2' or c == '3' or c == '4' or c == '5' or c == '6' or c == '7' or c == '8' or c == '9':
        
        found = True

    return found

def is_arithmetic(token_ptr):
    found = False

    match token_ptr:
        case '+':
            lex = "+"
            lex_name = "ADD_OP"

            found = True
            
        case '-':
            lex = "-"
            lex_name = "SUB_OP"

            found = True
            

        case '*':
            lex = "*"
            lex_name = "MULT_OP"

            found = True
            
        case '/':
            lex = "/"
            lex_name = "DIV_OP"

            found = True
            

        case '^':
            lex = "^"
            lex_name = "EXPON_OP"

            found = True
            
    
    return found

def is_literal(token_ptr):
    found = False

    if isdigit(line[1] == True):
        found = True
        found_numbers[0] = token_ptr
        lex_name = "INT_LITERAL"
        #count = 1;
        while is_digit(line[1]) == True:
            found_numbers+= line[1]
            line+=1
            #count++

    match token_ptr:
        case '(':
            lex = "("
            lex_name = "LEFT_PAREN"

            found = True
           

        case ')':
            lex = ")"
            lex_name = "RIGHT_PAREN"

            found = True
            

        case ';':
            lex = ";"
            lex_name = "SEMI_COLON"

            found = True
            


    return found
        
            
        

def is_equality(token_ptr):

    found = False

    match token_ptr:
        case '=':
            if line[1] == '=':
                line+=1
                lex = "=="
                lex_name = "EQUALS_OP"
            else:
                lex = "="
                lex_name = "ASSIGN_OP"

            found = True
            

        case '<':
            if line[1] == '=':
                line+=1
                lex = "<="
                lex_name = "LESS_THEN_OR_EQUAL_OP"
            else:
                lex = "<"
                lex_name = "LESS_THEN_OP"

            found = True
            

        case '>':
            if line[1] == '=':
                line+=1
                lex = ">="
                lex_name = "GREATER_THEN_OP"

            else:
                lex = ">"
                lex_name = "GREATER_THEN_OP"

            found = True
            

        case '!':
            if line[1] == '=':
                line+=1
                lex = "!="
                lex_name = "NOT_EQUALS_OP"
            else:
                lex = "!"
                lex_name = "NOT_OP"

            found = True
            
    
    return found

def main():
    input_line = None
    in_file = None
    out_file = None

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
        sys.exit(1)

    
    
    return 0


if __name__ == '__main__':
    main()
