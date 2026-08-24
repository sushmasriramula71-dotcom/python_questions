#Read a file containing numbers and use a for loop to print only the even numbers.
file=open("all_numbers.txt","w")
file.write("1\n""2\n""3\n""4\n""5\n""6\n""7\n""8\n""9\n")
file=open("all_numbers.txt","r")
for i in file:
    if int(i)%2==0:
        
        print(i.strip())