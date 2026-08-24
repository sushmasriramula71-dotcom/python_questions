lst=[10, 20, 10, 30, 20, 40, 30]
unique_list=[]
for i in lst:
    if i not in unique_list:
        unique_list.append(i)
print("The unique values of from the list is:",unique_list)