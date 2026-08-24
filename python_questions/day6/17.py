#Create a file containing 10 numbers. Use readlines() to calculate their average.
file=open("10numbers.txt","w")
file.write("1\n45\n89\n67\n34\n46\n87\n54\n82\n81")
file.close()
file=open("10numbers.txt","r")
numbers=file.readlines()
n=len(numbers)
sum=0

for i in numbers:
    sum+=int(i)
    avg=(sum)/n
    
print(avg)