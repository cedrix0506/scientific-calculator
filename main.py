#definimos las funciones para cada operacion

def add(number1, number2):
    return number1 + number2


def subtract(number1, number2):
    return number1 - number2


def multiply(number1, number2):
    return number1 * number2

def divide(number1, number2):
    if number2 == 0:
        raise ValueError("Cannot divide by zero")
    return number1 / number2


def power(number1, number2):
    return number1 ** number2


def integer_divide(number1, number2):
    if number2 == 0:
        raise ValueError("Cannot divide by zero")
    return number1 // number2


def modulus(number1, number2):
    if number2 == 0:
        raise ValueError("Cannot divide by zero")
    return number1 % number2

#titulo
print("=" * 30)
print("     CALCULATOR")
print("=" * 30)

#preguntar nombre y decir hola
name = input("Enter your name: ")
print(f"Hello, {name}! Welcome to the calculator.")

#Agregar un menu
print("MENU")

print("1. addition")
print("2. subtraction")
print("3. multiplication")
print("4. division")
print("5. power")   
print("6. integer division")
print("7. modulus")

#preguntar al usuario que operacion desea realizar
while True:
    try:
        operation = int(input("Enter the number of the operation: "))
        if 1 <= operation <= 7:
            break
        print("Invalid operation, please enter an integer between 1 and 7.")
    except ValueError:
        print("Invalid input, please enter a valid operation number.")

# Preguntar 2 números
while True:
    try:
        number1 = float(input("Enter the first number: "))
        number2 = float(input("Enter the second number: "))

        if operation in (4, 6, 7) and number2 == 0:
            print("Cannot divide by zero, please enter a different second number.")
            continue

        break

    except ValueError:
        print("Invalid input, please enter a valid number.")
    

#realizar la operacion e imprimir dependiendo de la opcion elegida
try:
    if operation == 1:
        result = add(number1, number2)
    elif operation == 2:
        result = subtract(number1, number2)
    elif operation == 3:
        result = multiply(number1, number2)
    elif operation == 4:
        result = divide(number1, number2)
    elif operation == 5:
        result = power(number1, number2)
    elif operation == 6:
        result = integer_divide(number1, number2)
    elif operation == 7:
        result = modulus(number1, number2)
    else:
        result = "Invalid operation"
except ValueError as error:
    result = str(error)

print(f" The result of the operation is: {result}")

