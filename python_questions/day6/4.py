#Create a file containing 5 numbers, one per line. Use readlines() to calculate their sum.
sum=0
file=open("numbers.txt","w")
file.write("1\n""2\n""3\n""4\n""5\n")
file=open("numbers.txt","r")

content=file.readlines()
for info in content:
    sum+=int(info)
print(sum)
file.close()