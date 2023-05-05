# cs352_project4
Authors: Daniel Aoulou, Laurin Burge  
Due Date: 05 May, 2023  

tokenizer.py is a lexical analyzer built for a simple provided example language.
The tokenizer reads lines from a file of input and prints an analysis of each lexeme
and statement in the input file to a seperate output file.

While in directory containing tokenizer.py,   

To run:  
`python3 tokenizer.py input_file output_file`  

Example:  
`python3 tokenizer.py unix_input.txt output.txt`  

The project folder contains the provided `unix_input.txt` and `unix_input_errors.txt` files.
`unix_input.txt` has been treated with dos2unix on Agora to remove carriage returns that were previously present.

## Functional Programming Features

**Recursion instead of iteration:**  
`read_next_line(file, outfile, this_line)`

**Pure function:**  
`increment_statements(i)`

**A function definition that calls another of your function
definitions with at least one function definition you wrote as an argument:**  
`check_white_space(token, fn)`

**Return a function definition you wrote as the return
value from a function definition that you wrote:**  
`write_to_file(token)`

**An anonymous function (that is, at least one lambda) that you wrote:**  
`add_to_statement`

