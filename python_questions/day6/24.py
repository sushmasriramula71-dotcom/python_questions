#Check whether a file exists
# Ask the user for a filename. Check whether the file exists before attempting to open it. Display an appropriate message depending on whether the file exists or not.
import os
filename = input("Enter the filename: ")
if os.path.exists(filename):
    print("File exists.")
    file = open(filename, "r")
    print(file.read())
    file.close()
else:
    print("File does not exist.")