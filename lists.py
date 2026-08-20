Numbers = [12, 5, 8, 21, 4, 15, 10]
max=Numbers[0]
small=Numbers[0]
sum=0
for i in Numbers:
    if i>max:
        max=i
    if i<small:
        small=i
    sum+=i
print("lar_num is: ",max)
print("Small_num is: ",small)
print("sum of all numbers is",sum)