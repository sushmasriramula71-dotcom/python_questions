list1=list(map(int,input("Enter list values").split(" ")))
large_num=list1[0]
small_num=list1[0]
for i in list1:
    if i<small_num:
        small_num=i
    if i>large_num:
        large_num=i
print(small_num)
print(large_num)
print(list1)
print(f"largest_num is{large_num} and smalles_number is {small_num}")