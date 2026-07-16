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
operation = int(input("Enter the number of the operation: "))

#preguntar 2 numeros
number1 = float(input ("Enter the first number :"))
number2 = float(input ("Enter the second number :"))

#definir operaciones
addition = number1 + number2
subtraction = number1 - number2
multiplication = number1 * number2
division = number1 / number2
power = number1 ** number2
integer_division = number1 // number2
modulus = number1 % number2

#realizar la operacion dependiendo de la opcion elegida
if operation == 1:
    result = addition
elif operation == 2:
    result = subtraction
elif operation == 3: 
    result = multiplication
elif operation == 4:
    result = division
elif operation == 5:
    result = power
elif operation == 6:
    result = integer_division
elif operation == 7:
    result = modulus    
else:
    result = "Invalid operation"
print(f" The result of the operation is: {result}")

