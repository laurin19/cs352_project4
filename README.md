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
Line 131: `read_next_line(file, outfile, this_line)`

**Pure function:**  
Line 120: `increment_statements(i)`

**A function definition that calls another of your function
definitions with at least one function definition you wrote as an argument:**  
Line 96: `check_white_space(token, fn)`

**Return a function definition you wrote as the return
value from a function definition that you wrote:**  
Line 68: `write_to_file(token)`

**An anonymous function (that is, at least one lambda) that you wrote:**  
Line 294: `lambda op: True if op == token_ptr else False, arithmetic`

**Closure that involves some state (that is, variable) that is being preserved 
and used within the closure using a function that you wrote:**  
Line 337: `pre_concat(c)`

**map():**  
Line 470: `result = list(map(add_to_equals, two))`

**filter():**  
Line 292: `filter()`

**reduce():**  
Line 407: `result = reduce(concat, nums, "")`

**list comprehension:**  
Line 454: `equality_ops = [x for x in operators if any(`
