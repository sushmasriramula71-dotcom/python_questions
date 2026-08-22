tuple1=(10, 20, 10, 30, 10, 40, 20)
sum=0
max_num=tuple1[0]
min_num=tuple1[0]
for i in tuple1:
    sum+=i
    if i>max_num:
        max_num=i
    if i<min_num:
        min_num=i
print(f"sum is {sum}, maximum value is {max_num}, minimum value is {min_num}")
    

