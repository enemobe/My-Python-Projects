import math

print("Welcome to CalcWorm")
print("What can we do for you today?")
print("Options:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")
print("6. Exponential")
print("7. Logarithm\n")

while True:
    operation = input("Enter the operation you wish to perform [1-7]: ")
    print("If Logarithm operation is selected, then input base as first number and target number as second number")
    user_input = operation
    if user_input.isdigit() and 1 <= int(user_input) <= 7:
        operation = int(user_input)
        break
    else:
        print("Invalid input. Please enter an option between 1 and 7.")

while True:
    num1 = input("Enter first number: ")
    if num1.isdigit() or (num1.startswith('-') and num1[1:].isdigit()):
        num1 = float(num1)
        break
    print("Invalid input. Can only contain numbers, please enter a valid number.")

while True:
    num2 = input("Enter second number: ")
    if num2.isdigit() or (num2.startswith('-') and num2[1:].isdigit()):
        num2 = float(num2)
        break
    print("Invalid input. Can only contain numbers, please enter a valid number.")

if operation == 1:
    result = num1 + num2
elif operation == 2:
    result = num1 - num2
elif operation == 3:
    result = num1 * num2
elif operation == 4:
    result = num1 / num2
elif operation == 5:
    result = num1 % num2
elif operation == 6:
    result = num1 ** num2
elif operation == 7:
    result = math.log(num2, num1)
else:
    result = None
    print("O foolish user, why did you not select a valid option?")

if result is None:
    pass
else:
    print(f"The result is {result}")
