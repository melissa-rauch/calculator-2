"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

while True:
    #get user equation
    user_input = input("Enter your equation > ")
    #tokenize user input
    tokens = user_input.split(" ")
    
    #create break if they want to quit
    #create break if they want to quit
    #assign variables to tokens  
    #factor in if there are > than 2 tokens
    #pass arithmatic functions
    #add float
