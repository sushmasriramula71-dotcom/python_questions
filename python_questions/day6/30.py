# File + Exception Handling Challenge
#  Create a program that asks the user for a filename and a number.

filename = input("Enter the filename: ")
try:
    num = int(input("Enter a numb: "))
    file = open(filename, "r")
    print("File content:")
    print(file.read())
    print("Your number is:", num)
    file.close()
except FileNotFoundError:
    print("File does not exist.")
except ValueError:
    print("Invalid input! Please enter a valid number.")
except Exception as e:
    print("An unexpected error occurred:", e)