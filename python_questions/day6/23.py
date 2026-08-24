#Overwrite an existing file
 #Create a file containing some old information. Ask the user for new information and use "w" mode to replace the old content completely. Read the file afterward to verify the change.
   
file = open("info.txt", "w")
file.write("Old information\n")
file.write("This information will be replaced.\n")
file.close()
new_info = input("Enter new information: ")
file = open("info.txt", "w")
file.write(new_info + "\n")
file.close()
file = open("info.txt", "r")
for line in file:
    print(line, end="")
file.close()