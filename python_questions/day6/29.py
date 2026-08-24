# Handle file errors
#  Ask the user for a filename and attempt to open it in read mode. Handle the situation where:
# The file doesn't exist.
# Another unexpected error occurs.

filename = input("Enter the filename: ")
file = open(filename, "r")
try:
    print(file.read())
    file.close()
except FileNotFoundError:
    print("File does not exist.")
except Exception as e:
    print("An unexpected error occurred:", e)