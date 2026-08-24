file=open("Numbers.txt","w")
for num in range(5):
    num=int(input("Enter a value: "))
    file.write(str(num)+"\n")
file=open("Numbers.txt","r")
numbers=file.read()
print(numbers)