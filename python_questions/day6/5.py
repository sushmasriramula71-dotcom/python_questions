#Create a file containing three lines. Use readline() to read and print each line separately.
file=open("threelines","w")
file.write("Rahul 80\n""Aman 35\n""Priya 92")
file=open("threelines","r")
content=file.readlines()
for line in content:
    print(line.strip())