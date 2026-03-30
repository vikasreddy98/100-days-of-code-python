from art import logo
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def calculator():
    calc_on = True
    print(logo)
    first_num = float(input("What's the first number?: "))
    while calc_on:
        for s in operations:
            print(s)
        operator = input("Pick an operation: ")
        second_num = float(input("What's the next number?: "))
        answer = operations[operator](first_num, second_num)
        print(f"{first_num} + {second_num} = {answer}")
        cont_calc = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to star a new calculation: ")
        if cont_calc == "y":
            first_num = answer
        else:
            calc_on = False
            print("\n" * 20)
            calculator()

calculator()