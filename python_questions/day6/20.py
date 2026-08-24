#Create a program that:
# Takes 5 student names from the user.
# Writes them to a file.
# Reads the file using a for loop.
# Prints each student with a serial number.

file=open("details.txt","w")
for n in range(5):
    name=input("Enter your name: ")
    
    file.write(name+"\n")
    
file.close()
file=open("details.txt","r")
info=file.read()
print(info)