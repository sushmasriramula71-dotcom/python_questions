file=open("student.txt","w")
file.write("Sushma " \
"22 " \
"software_trainee")
file=open("student.txt","r")
cont=file.read()
print(cont)