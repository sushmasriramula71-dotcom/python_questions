
file = open("students.txt", "w")
file.write("Sushma\n")
file.write("Rahul\n")
file.write("Priya\n")
file.close()
file = open("students.txt", "a")
for i in range(2):
    name = input("Enter student name: ")
    file.write(name + "\n")
file.close()
file = open("students.txt", "r")
for line in file:
    print(line, end="")
file.close()