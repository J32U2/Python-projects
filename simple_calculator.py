''' this function takes 2 numbers as well as an operator
math operator must be included between quotes ("")'''

def calc(num1,operation,num2):
    print("your answer is: ")
    if operation == "-" :
        return num1 - num2
    elif operation == "+" :
        return num1 + num2
    elif operation == "x" or "*" :
        return num1 * num2
    elif operation == "/" :
        return num1 / num2
    elif operation == "//" :
        return num1 // num2
    elif operation == "**" :
        return num1 ** num2
