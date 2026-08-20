n=int(input("enter n value: "))
cnt=0
n=str(n)
for i in n:
    if int(i)%2==0:
        cnt+=1
print(cnt)