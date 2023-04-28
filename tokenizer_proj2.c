/**                                                                             
 * CS352 Project 2: Lexical Analyzer
 * Authors: Zach Eanes and Laurin Burge.
 *
 * In this file, we lay out all of the main logic used in order to create a lexical
 * analysis of our defined alphabet. We do this by identifying each proper token in a
 * given input file, both that are valid and invalid in our alphabet, and displaying 
 * the output to a provided output file as well.                                   
 *                                                                              
 * NOTE: The terms 'token' and 'lexeme' are used interchangeably in this        
 *       program.                                                               
 *                                                                                                                      
 * @version March 24, 2023                                                      
 */                                                                             
#include <stdio.h>                                                              
#include <string.h>                                                             
#include <stdlib.h>                                                             
#include <ctype.h>                                                              
#include "tokenizer.h"
                                                                                
/* global variables */                                                             
char *line; /* Global pointer to line of input */                     
                                                                                
/* our three optional global variables */               
char *lex; /* Most recently identified lexeme */                                
char *lex_name; /* name of the lex identified */
char found_numbers[TSIZE]; /* place to store found numbers */

/**
 * Main driver for our program. Processes input file, grabs each line, and identifies lexemes.
 * @param argc count of the number of arguments passed in
 * @param argv char* array of all the inputs from the command line
 */
int main(int argc, char* argv[]){
    //int current_lex;       /* Count of the current statement */
    //char  token[TSIZE];      /* Spot to hold a token, fixed size */
    char  input_line[LINE];  /* Line of input, fixed size */
    FILE  *in_file = NULL;   /* input file pointer */
    FILE  *out_file = NULL;  /* output file pointer */
    //int   line_count,      /* Number of lines read */
    int   start,             /* is this the start of a new statement?; used to establish new statements */
    count;             /* count of tokens in the array */

    /* NOTE ON ABOVE VARS: We didn't find a need for some of the vars, but instead of removing
     *                     we decided to leave them there as they were included with the given
     *                     file.        */

    if (argc != 3) {
        printf("Usage: tokenizer inputFile outputFile\n");
        exit(1);
    }
    in_file = fopen(argv[1], "r");
    if (in_file == NULL) {
        fprintf(stderr, "ERROR: could not open %s for reading\n", argv[1]);
        exit(1);
    }
    out_file = fopen(argv[2], "w");
    if (out_file == NULL) {
        fprintf(stderr, "ERROR: could not open %s for writing\n", argv[2]);
        exit(1);
    }
    start = 1; /* Statement counter initialized */
    count = 0; /* count of the current lex in a statement */
    while(fgets(input_line, LINE, in_file) != NULL){
        line = input_line;  /* Sets a global pointer to the memory location */
        /* where the input line resides */

        while(*line != '\0'){
            if(count == 0 && isspace(*line) == FALSE){ /* initial statement is printed */
                statement_prompt(out_file, start);     /* whenever our count is reset */
                start++;
            }

            if(isspace(*line) == FALSE){ /* character isn't white space, so we grab token */
                get_token(line);

            }

            /* Use isspace to ensure spaces are skipped */
            if(strcmp(lex_name, "ERROR") == 0 && isspace(*line) == FALSE){
                lex_error(out_file, lex);
            }
            else if(isspace(*line) == FALSE && strcmp(lex_name, "INT_LITERAL") != 0){
                update(lex, lex_name, out_file, count);
                count++;
            }
            else if(isspace(*line) == FALSE && strcmp(lex_name, "INT_LITERAL") == 0){
                update(found_numbers, lex_name, out_file, count);
                count++;
                memset(found_numbers, '\0', sizeof(found_numbers)); /* reset numbers array */
            }

            if(strcmp(lex_name, "SEMI_COLON") == 0){ /* Reset count at end of a statement */
                count = 0;
            }
            line++; /* increment line pointer to identify the next token */
        }
    }
    fclose(in_file);
    fclose(out_file);
    return 0;
}

/**                                                                             
 * This function identifies the type of lexeme that has been passed in and prints
 * a message describing and identifying the lexeme.
 * @param token_ptr pointer to the token to be identified                       
 */                                                                             
void get_token(char *token_ptr){                                                
    int result = is_arithmetic(token_ptr);
    if(result == FALSE){ /* Check to see if lex hasn't been identified yet */
        result = is_equality(token_ptr);
        if(result == FALSE){
            result = is_literal(token_ptr);
        }
    }
    if(result == 0){ /* If lex was never identified, display as error */
        lex = token_ptr;
        lex_name = "ERROR";
    }
}

/* BLOCK OF ALL FUNCTIONS THAT ARE RESPONSIBLE FOR OUTPUTTING TO FILE */

/**                                                                             
 * This function increments necessary ints whenever a lexeme is added, such as count
 * and start, and prints our lexeme message to the output file.
 * @param curr_token    current character that was identified                   
 * @param lex_type      string representing the lexeme type.                    
 * @param out_file      file to output print to                                 
 * @param current_count count in the current statement                          
  *                                                                              
 */
void update(char *curr_token, char *lex_type, FILE *out_file, int current_count){

    if(is_vowel(lex_type[0]) == TRUE){ /* Check when to use an if there's a vowel */
        fprintf(out_file, "Lexeme %d is %s and is an %s\n", current_count, curr_token, lex_type);

    }else{ /* Use a when it's not a vowel */
        fprintf(out_file, "Lexeme %d is %s and is a %s\n", current_count, curr_token, lex_type);
    }
    /* Display end of statement break whenever we find a semicolon */
    if(strcmp(lex_name, "SEMI_COLON") == 0){ /* When the strings are equal, end curr statement. */
        fprintf(out_file, "---------------------------------------------------\n");
    }
}

/**
 * This function prints out the necessary message given when a new statement occurs.
 */
void statement_prompt(FILE* out_file, int start){
    fprintf(out_file, "Statement #%d\n", start);
}

/**
 * This function outputs to the correct file a message whenever a lexical error is
 * identified.
 * @param token character identified as an error
 * @param output file to be written to
 */
void lex_error(FILE *out_file, char *token){
    fprintf(out_file, "===> '%c'\nLexical error: not a lexeme\n", *token);
}

/* BLOCK OF ALL THE IDENTIFYING FUNCTIONS */

/**
 * This function determines if a passed in character is a vowel or not. This is used
 * to determine when we need to output "a" or "an" in our update function.
 * @param c character to be checked if a vowel or not.
 * @return  1 whenever the character is a vowel, 0 otherwise
 */
int is_vowel(char c){
    int found = 0;
    char to_check = tolower(c); /* Make the function case insensitive */
    if((to_check == 'a') | (to_check == 'e') | (to_check == 'i') |
       (to_check == 'o') | (to_check == 'u')){
        found = 1; /* vowel found */
    }
    return found;
}
/**
 * This function determines if a passed in character is a digit or not.
 * @param c character to be checked if a digit or not.
 * @return  1 when the character is a digit, 0 otherwise
 * 
 * NOTE ON THIS FUNCTION:
 *  Whenever this was loaded into agora, we had to define a method to find a digit
 *  even though a method exists already in <ctype.h>. Not sure why this occurred,
 *  but for ensuring this works everywhere, we defined this method itself.
 */
int is_digit(char c){
    int found = 0;
    if((c == '0') | (c == '1') | (c == '2') | (c == '3') |
       (c == '4') | (c == '5') | (c == '6') | (c == '7') |
       (c == '8') | (c == '9')){
        found = 1; /* digit identified */
    }
    return found;
}

/**                                                                             
 * This function identifies the lexeme if it is a type of arithmetic. This includes:
 * - addition operator (+)                                                      
 * - subtraction operator (-)                                                   
 * - multiplication operator (*)                                                
 * - division operator (/)                                                      
 * - exponent operator (^)
 * @param token_ptr pointer to the token to be identified                       
 * @return 1 if an arithmetic, 0 otherwise                                      
 */                                                                             
int is_arithmetic(char *token_ptr){                                             
    int found = 0; /* changed to 1 if a lexeme is found */
    switch(*token_ptr){                                                         
        case '+':                                                               
            lex = ADD_OP; /* update the current lex, name for the lex, changes return val */                                               
            lex_name = "ADD_OP";                                                
            found = 1;                                                          
            break;                                                              
        case '-':                                                               
            lex = SUB_OP;                                                       
            lex_name = "SUB_OP";                                                
            found = 1;                                                          
            break;                                                              
        case '*':                                                               
            lex = MULT_OP;                                                      
            lex_name = "MULT_OP";                                               
            found = 1;                                                          
            break;                                                              
        case '/':                                                               
            lex = DIV_OP;                                                       
            lex_name = "DIV_OP";                                                
            found = 1;                                                          
            break;                                                              
        case '^':                                                               
            lex = EXPON_OP;                                                     
            lex_name = "EXPON_OP";                                              
            found = 1;                                                          
            break;                                                              
    }                                                                           
    return found;                                                               
}
                                                                                
/**                                                                             
 * This function identifies the lexeme if it is a type of literal. This includes:
 * - left parentheses ('(')                                                     
 * - right parentheses (')')                                                    
 * - semicolons (;)                                                             
 * - integer literals ([0-9]+)
 * @param token_ptr pointer to the token to be identified.                      
 * @return 1 if an arithmetic, 0 otherwise                                      
 */                                                                             
int is_literal(char *token_ptr){                                                
    int found = 0; /* changed to 1 if lex is found */                           
    if(is_digit(*token_ptr) == TRUE){ /* if current token is a digit */
        found = 1; /* number has been found */
        found_numbers[0] = *token_ptr; /* store in char array of numbers */
        lex_name = "INT_LITERAL";
        int cnt = 1; /* cnt used to place into char array of numbers */
        while(is_digit(line[1]) == TRUE){ /* continue adding to array while we have digits */
            found_numbers[cnt] = line[1];
            line++; /* increment line pointer so above logic continues to work */
            cnt++;
        }
    }
    switch (*token_ptr){
        case '(':
           lex = LEFT_PAREN;
            lex_name = "LEFT_PAREN";
            found = 1;
            break;
        case ')':
            lex = RIGHT_PAREN;
            lex_name = "RIGHT_PAREN";
            found = 1;
            break;
        case ';':
            lex = SEMI_COLON;
            lex_name = "SEMI_COLON";
            found = 1;
            break;
    }
    return found;                                                               
}

/**                                                                             
 * This function identifies the lexeme if it's a type of equality. This includes:
 * - assignment operator (=)                                                    
 * - less then operator (<)                                                     
 * - less then equal operator (<=)                                              
 * - greater then operator (>)                                                  
 * - greater then equal operator (>=)                                           
 * - not operator (!)                                                           
 * - not equal operator (!=)
 * @param token_ptr pointer to the token to be identified                       
 * @return 1 if an arithmetic, 0 otherwise                                      
 */                                                                             
int is_equality(char *token_ptr){                                               
    int found = 0; /* changed to 1 if lex is found */
    switch(*token_ptr){                                                         
        case '=':                                                               
            if(line[1] == '='){ /* be greedy and check next immediately */                                                 
                line++;                                                         
                lex  = EQUALS_OP;                                               
                lex_name = "EQUALS_OP";                                         
            }else{ /* if following token isn't an =, it's just assign op */                                                             
                lex = ASSIGN_OP;                                                
                lex_name = "ASSIGN_OP";                                         
            }                                                                   
            found = 1;                                                          
            break;                                                              
        case '<':                                                               
            if(line[1] == '='){                                                 
                line++;                                                         
                lex  = LESS_THEN_OR_EQUAL_OP;                                   
                lex_name = "LESS_THEN_OR_EQUAL_OP";                             
            }else{ /* if next token isn't =, it's just a less then op */                                                             
                lex = LESS_THEN_OP;                                             
                lex_name = "LESS_THEN_OP";                                      
            }                                                                   
            found = 1;                                                          
            break;                                                              
        case '>':                                                               
            if(line[1] == '='){                                                 
                line++;                                                         
                lex = GREATER_THEN_EQUAL_OP;                                    
                lex_name = "GREATER_THEN_EQUAL_OP";                             
            }else{ /* if next token isn't =, it's just a greater then op */                                                             
                lex = GREATER_THEN_OP;                                          
                lex_name = "GREATER_THEN_OP";                                   
            }                                                                   
            found = 1;                                                          
            break;                                                              
        case '!':                                                               
            if(line[1] == '='){                                                 
                line++;                                                         
                lex = NOT_EQUALS_OP;                                            
                lex_name = "NOT_EQUALS_OP";                                     
            }else{ /* if next token isn't =, it's just a not op */
                lex = NOT_OP;                                                   
                lex_name = "NOT_OP";                                            
            }                                                                   
            found = 1;                                                          
            break;                                                              
    }                                                                           
    return found;                                                               
}