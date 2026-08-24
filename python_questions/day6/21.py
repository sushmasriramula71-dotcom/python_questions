#Append to an existing file
# Create notes.txt containing some text. Take a new sentence from the user and append it to the existing file using "a" mode. Then read and display the complete file.

file = open("notes.txt", "w")
file.write("This is my first note.\n")
file.close()
sentence = input("Enter a new sentence: ")
file = open("notes.txt", "a")
file.write(sentence + "\n")
file.close()
file = open("notes.txt", "r")
for line in file:
    print(line, end="")
file.close()