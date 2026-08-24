file=open("Names.txt","w")
for n in range(5):
    name=input("Enter name")
    file.write(name+"\n")
file=open("Names.txt","r")
names=file.read()
print(names)