"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

while True:
    #get user equation
    user_input = input("Enter your equation > ")
    #tokenize user input
    tokens = user_input.split()
    #create break if they want to quit
    if "q" in tokens:
        print("Goodbye")
        break
    #assign variables to tokens    
    operator = tokens[0]
    num1 = tokens[1]

    #factor in if there are > than 2 tokens
    if len(tokens) == 3:
        num2 = tokens[2]
    if len(tokens) > 3:
        num3 = tokens[3]
    result = None

    #pass arithmatic functions
    #add float
    if operator == "+":
        result = add(float(num1), float(num2))
    if operator == "-":
        result = subtract(float(num1), float(num2))
    if operator == "*":
        result = multiply(float(num1), float(num2))
    if operator == "/":
        result = divide(float(num1), float(num2))    
    if operator == "square":
        result = square(float(num1), float(num2))
    if operator == "cube":
        result = cube(float(num1))
    if operator == "power":
        result = power(float(num1), float(num2))
    if operator == "mod":
        result = mod(float(num1), float(num2))
    
    print(result)
