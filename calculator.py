print("Hi! I'm a calculator. Please insert two numbers and the operation you want to perform on them.")
number_one = int(input("Write your first number here: "))
number_two = int(input("Write your second number here: "))
operation = input("Would you like to +, -, / or *? ")

if operation == "+":
    print("Your result is " + str(number_one + number_two) + ".")
elif operation == "-":
    print("Your result is " + str(number_one - number_two) + ".")
elif operation == "/":
    print("Your result is " + str(number_one / number_two) + ".")
elif operation == "*":
    print("Your result is " + str(number_one * number_two) + ".")
else:
    print("There's been an error - please check your syntax.")
