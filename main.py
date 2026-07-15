#titulo
print("=" * 30)
print("     CALCULATOR")
print("=" * 30)

#preguntar nombre y decir hola
name = input("Enter your name: ")
print(f"Hello, {name}! Welcome to the calculator.")

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

#encabezado de resultados
print("\nResults:")
print("=" * 30)

#imprimir operaciones
print(f" Addition of {number1} and {number2} is : {addition}")
print(f" Subtraction of {number1} and {number2} is : {subtraction}")
print(f" Multiplication of {number1} and {number2} is : {multiplication}")
print(f" Division of {number1} and {number2} is : {division}")
print(f" Power of {number1} and {number2} is : {power}")
print(f" Integer Division of {number1} and {number2} is : {integer_division}")
print(f" Modulus of {number1} and {number2} is : {modulus}")