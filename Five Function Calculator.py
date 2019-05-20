def addition():
    number1 = float(input("Enter a number: "))
    number2 = float(input("Enter a number: "))
    sum = number1 + number2
    print(str(number1) + " + " + str(number2) + " = " + str(sum))

def subtraction():
    number1 = float(input("Enter a number: "))
    number2 = float(input("Enter a number: "))
    difference = number1 - number2
    print(str(number1) + " - " + str(number2) + " = " + str(difference))
    
def multiplication():
    number1 = float(input("Enter a number: "))
    number2 = float(input("Enter a number: "))
    product = number1 * number2
    print(str(number1) + " • " + str(number2) + " = " + str(product))

def division():
    number1 = float(input("Enter a number: "))
    number2 = float(input("Enter a number: "))
    quotient = number1/number2
    print(str(number1) + " ÷ " + str(number2) + " = " + str(quotient))

def modulus():
    number1 = float(input("Enter a number: "))
    number2 = float(input("Enter a number: "))
    remainder = number1%number2
    print(str(number1) + " % " + str(number2) + " = " + str(remainder))

def calculator():
    option = input("Calculate addition, subtraction, multiplication, divsion, modulus? ")
    option = option.lower()
    if option == "addition":
        addition()
    if option == "subtraction":
        subtraction()
    if option == "multiplication":
        multiplication()
    if option == "division":
        division()
    if option == "modulus":
        modulus()

calculator()
    
