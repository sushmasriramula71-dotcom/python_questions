# Handle invalid number input
#  Ask the user to enter two numbers and calculate their sum. Handle the situation where the user enters text instead of a number using try-except.
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    sum = num1 + num2
    print("Sum =", sum)
except ValueError:
    print("Invalid input! Please enter numbers only.")