line = None
lex = None
lex_name = None
found_numbers = []

import sys


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