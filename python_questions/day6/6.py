#A file contains a student's name, age, and marks on separate lines. Use readline() to read all three values and display them.
file=open("stud_marks.txt","w")
file.write("Sushma 45\n""Saiprasnna 43\n""Thrisha 43")
file=open("stud_marks.txt","r")

for line in range(4):
    content=file.readline()
    print(content.strip())