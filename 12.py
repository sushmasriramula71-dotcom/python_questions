num=int(input("Enter a value: "))
if num<0:
    print(f"{num} is not prime")
else:
    for i in range(2,num):
        if num%i==0:
            
            print(f"{num} is not prime")
    else:
        print(f"{num} is prime")