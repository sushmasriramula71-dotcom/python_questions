#Delete a file
# Ask the user for a filename and delete that file. If the file doesn't exist, display an appropriate message instead of allowing the program to crash.
import os
filename = input("Enter the filename to delete: ")
if os.path.exists(filename):
    os.remove(filename)
    print("File deleted successfully.")
else:
    print("File does not exist.")