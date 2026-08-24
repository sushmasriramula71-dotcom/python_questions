# Handle division errors
#  Ask the user for two numbers and divide the first by the second. Handle:
# Invalid number input
# Division by zero
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

  
try:
    result = num1 / num2
   
    print("Result =", result)
except ValueError:
    print("Invalid input! Please enter numbers only.")
except ZeroDivisionError:
    print("Cannot divide by zero!")