"""
CS352 Project 4: Functional Programming

This program models a lexical analyzer but uses functional programming concepts
to accomplish this.

Authors: Laurin Burge and Daniel Aoulou

Date: 5/5/23

"""

line = []
lex = ""
lex_name = " "
statement = []
stmt_counter = 1
found_numbers = ""
out_file = None

import sys
from functools import partial, reduce


def get_token(token):
    """ This function identifies the type of lexeme that has been passed in
        and prints a message describing and identifying the lexeme.

    Args:
        string token: the token to be identified

    """
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


def process_statement(statement):
    """This function writes statements and calls necessary functions to write
       to the outfile

    Args:
        list statement: The list the holds the tokens from the input file line

    """

    global out_file, lex_name
    out_file.write("Statement #" + str(stmt_counter) + "\n")
    counter = 0
    for x in statement:
        lex_name = "ERROR"
        file_updater = write_to_file(x)
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print(x)
        file_updater(lex, lex_name, out_file, counter)
        if lex_name is not "ERROR": counter += 1
        # out_file.write(x)


def write_to_file(token):
    """
    Args:
        string token: the token that we are currently looking at

    Returns:
        update: a function that will update and write the lexemes and their
                name, etc to the outfile


    """
    global lex
    if (
            # is_digit(token)
            is_literal(token)
            or is_equality(token)
            or is_arithmetic(token)
    ):
        return update
    elif token is None:
        return statement_prompt
    else:
        lex = token
        return update


# function definition which calls another function definition
# with at least one function definition
def check_white_space(token, fn):
    """This function checks to see if the token is a white space character

    Args:
        string token: the string



    """
    if token != ' ' and token != '\n' and token != '\t':
        fn(token)


def add_to_statement(token):
    """Adds a token to the statement list

    Args:
        string token: a string that will be added to a list
    """

    statement.append(token)


# pure function
def increment_statements(i):
    """Increments the param by 1

    Args:
        int i: the int you want to increment

    """
    return i + 1


# recursion
def read_next_line(file, outfile, thisline):
    """ Reading the file in line by line

    Args:
        file: the input file

        file outfile: the file to write to

        list thisline: the current line

    """

    global statement

    lineLength = len(thisline)
    for i in range(lineLength):
        get_token(thisline[i])

    # outfile.writelines(thisline)

    nextLine = file.readline()
    if not nextLine:
        process_statement(statement)
        return 0
    else:
        read_next_line(file, outfile, nextLine)


def update(curr_token, lex_type, out_file, current_count):
    """This function increments necessary ints whenever a lexeme is added
        and prints our lexeme message to the output file.

    Args:
        string curr_token: current character that was identified

        string lex_type: string representing the lexeme type

        file out_file: file to output to

        int current_count: the lexeme count

    """
    global lex
    if lex_type is "ERROR":
        out_file.write("===> '" + lex + "'\nLexical error: not a lexeme\n")
        return 0

    if is_vowel(lex_type[0]) == True:
        out_file.write(
            "Lexeme " + str(current_count) + " is " + curr_token + " and is an " + lex_type + "\n"
        )
    else:
        out_file.write(
            "Lexeme " + str(current_count) + " is " + curr_token + " and is a " + lex_type + "\n"
        )

    if lex_name == "SEMI_COLON":
        out_file.write("________________________________")


def statement_prompt(out_file, start):
    """ This function prints otu the necessary message given when a new
        statement occurs.
    Args:
        file out_file: file to be written to

        int start: The line number

    """
    out_file.write("Statement " + str(start) + "\n")


def is_vowel(c):
    """ Checks to see if the param is a vowel or not
    Args:
        string c: The string to check
    Returns:
        boolean: True if the param was a vowel and false otherwise

    """

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
    # global lex
    """ Checks to see if the param is a number
    Args:
        string c: The string to check
    Returns:
        boolean: True if the param was a number and false otherwise

    """
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


# filter used here
def is_arithmetic(token_ptr):
    """ This function identifies the lexeme if it is a type of arithmetic
        So it could be +, -, *, /, ^
    Args:
        string token_ptr: The token to be identified

    Returns:
        boolean found: True if the token is an arithmetic lexeme, false otherwise

    """

    found = False
    global lex_name
    global lex

    arithmetic = ['+', '-', '*', '/', '^']

    print(token_ptr)
    # global line

    # filter used here
    result = list(filter(lambda op: True if op == token_ptr else False, arithmetic))
    print("in is_arithmetic")
    print(result)
    print(len(result))
    if len(result) > 0:
        found = True

        if token_ptr == '+':
            lex = "+"
            lex_name = "ADD_OP"

        elif token_ptr == '-':
            lex = "-"
            lex_name = "SUB_OP"

        elif token_ptr == '*':
            lex = "*"
            lex_name = "MULT_OP"

        elif token_ptr == '/':
            lex = "/"
            lex_name = "DIV_OP"


        elif token_ptr == '^':
            lex = "^"
            lex_name = "EXPON_OP"

        print(result)
    print(lex_name)
    print("in is_ARTH")
    return found


def concat(c, c2):
    """ This function concatenates 2 strings together
    Args:
        string c: the first string to concatenate
        string c2: the second string to concatenate

    Returns:
        string: the concatenated string of both arguments

    """
    c = c + c2
    return c

#closure
def pre_concat(c):
    """ This function returns another function loaded with a character
    to be concated to

        """
    first_char = c
    def post_concat(c2):
        return first_char + c2

    return post_concat


def check_for_eq(token_ptr):
    """This function checks to see if the parameter is an equal sign or not.

    Args:
        string token_ptr: The string to check if the param is an equals sign

    Returns:
        boolean: True if the param is an '=' and false otherwise
    """
    if token_ptr == '=':
        return True
    else:
        return False

    # reduce used here


def is_literal(token_ptr):
    """ This function identifies the lexeme if it is a type of literal.
        So it could be (, ), ;, or int literals
    Args:
        string token_ptr: The token to be identified

    Returns:
        boolean found: True if the token is an literal lexeme, false otherwise

    """

    found = False
    global lex_name
    global lex
    global statement
    # global found_numbers

    print("in is_literal")
    print(line)

    print(token_ptr)
    print(is_digit(token_ptr))

    nums = []
    # token_index = statement.index(token_ptr)
    if is_digit(token_ptr) == True:
        token_index = statement.index(token_ptr)
        # token_index = statement.index(token_ptr)
        found = True
        # result = reduce(concat, token_ptr, "")
        lex_name = "INT_LITERAL"

        index = statement.index(token_ptr)

        while is_digit(statement[index]) == True:

            if index > 0 and is_digit(statement[index - 1]):

                nums.append(statement.pop(index))

            else:
                nums.append(statement[index])
                index += 1
            # statement.pop(index)
            # print(statement[index])
            # index+=1
            # statement.pop(index)
            # also remove them from the list
        # reduce here
        result = reduce(concat, nums, "")

        lex = result
        statement[token_index] = result

        # while is_digit() == True:
        # functools.reduce(concat, line[1], 0)
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


# map used in here
def is_equality(token_ptr):
    """ This function identifies the lexeme if it is a type of equality
        So it could be =, ==, <, <=, >, >=, !, !=
    Args:
        string token_ptr: The token to be identified

    Returns:
        boolean found: True if the token is an equality lexeme, false otherwise

    """

    global statement
    global lex_name
    global lex
    found = False

    two = []

    print("in is_equality")
    print(statement)
    # token_index = statement.index(token_ptr)
    # REMOVE IT
    if token_ptr == "=":
        token_index = statement.index(token_ptr)
        if check_for_eq(statement[token_index + 1]) == True:
            two = ['', '']
            add_to_equals = pre_concat('=')

            # map here
            result = list(map(add_to_equals, two))

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
            # map here
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
            # map here
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
            # map here
            result = list(map(concat_with_found_numbers, two))

            print("--------------------------------------")
            print(result)

            result[0] = result[0] + result[1]
            lex = result[0]

            lex_name = "NOT_EQUALS_OP"
            statement[token_index] = result[0]
            print(statement[token_index])
            print(statement[token_index - 1])
            print(statement[token_index + 1])
            statement.remove('=')

        else:
            lex = "!"
            lex_name = "NOT_OP"

        found = True

    return found


def main():
    """Main function of the program. Checks to see if the user put the correct
       number of command line arguments and calls the function to read in the
       input from the input file.

    Returns:
        int: 0
    """
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


