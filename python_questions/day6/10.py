#Read a file containing numbers and find the largest and smallest number using a for loop.
file=open("all_numbers.txt","r")
max_num=None
min_num=None
for num in file:
    num=int(num)
    if max_num is None or num>max_num:
        max_num=num
    if min_num is None or num<min_num:
        min_num=num
print(min_num)
print(max_num)


# file = open("all_numbers.txt", "r")
# max_num = None
# min_num = None

# for num in file:

#     num = int(num)

#     if max_num is None or num > max_num:
#         max_num = num

#     if min_num is None or num < min_num:
#         min_num = num

# print(min_num)
# print(max_num)

# file.close()