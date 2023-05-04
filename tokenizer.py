line = []
lex = None
lex_name = None
statement = []
stmt_counter = 1
found_numbers = ""
out_file = None

import sys


def get_token(token):
    # line
    global lex
    global lex_name
    global statement
    global stmt_counter

    # print("in get_token")
    if token != ' ' and token != '\n' and token != '\t':
        statement.append(token)
    if token == ';':
        process_statement(statement)
        out_file.write("\n")
        statement = []
        stmt_counter += 1


def process_statement(statement):
    global out_file
    for x in statement:
        out_file.write(x)

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
    if is_vowel(lex_type[0]) == True:
        out_file.write(
            "Lexeme", current_count, "is", curr_token, "and is an", lex_type, "\n"
        )
    else:
        out_file.write(
            "Lexeme", current_count, "is", curr_token, "and is a", lex_type, "\n"
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

    return found


def is_arithmetic(token_ptr):
    found = False

    if token_ptr == "+":
        lex = "+"
        lex_name = "ADD_OP"

        found = True

    elif token_ptr == "-":
        lex = "-"
        lex_name = "SUB_OP"

        found = True

    elif token_ptr == "*":
        lex = "*"
        lex_name = "MULT_OP"

        found = True

    elif token_ptr == "/":
        lex = "/"
        lex_name = "DIV_OP"

        found = True

    elif token_ptr == "^":
        lex = "^"
        lex_name = "EXPON_OP"

        found = True

    return found


def is_literal(token_ptr):
    found = False
    global line
    global found_numbers
    if is_digit(line[1] == True):
        found = True
        found_numbers[0] = token_ptr
        lex_name = "INT_LITERAL"
        # count = 1;
        while is_digit(line[1]) == True:
            found_numbers += line[1]
            line += 1
            # count++

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

    found = False
    if token_ptr == "=":
        if line[1] == "=":
            line += 1
            lex = "=="
            lex_name = "EQUALS_OP"
        else:
            lex = "="
            lex_name = "ASSIGN_OP"

        found = True

    elif token_ptr == "<":
        if line[1] == "=":
            line += 1
            lex = "<="
            lex_name = "LESS_THEN_OR_EQUAL_OP"
        else:
            lex = "<"
            lex_name = "LESS_THEN_OP"

        found = True

    elif token_ptr == ">":
        if line[1] == "=":
            line += 1
            lex = ">="
            lex_name = "GREATER_THEN_OP"

        else:
            lex = ">"
            lex_name = "GREATER_THEN_OP"

        found = True

    elif token_ptr == "!":
        if line[1] == "=":
            line += 1
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

