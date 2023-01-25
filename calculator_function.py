from calculatorart import logo
print("Calculator Using Python",logo)

#Functions for calculations
def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

calculator_operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

n1 = int(input("Enter a First number: "))
n2 = int(input("Enter a second number: "))

for operations in calculator_operations:
    print(operations)
    
user_choice = input("Which operation do you want to perform ? Pick from above line \n")

calculation = calculator_operations[user_choice]
answer = calculation(n1,n2)
    
print(f"{n1} {user_choice} {n2} = {answer}")

