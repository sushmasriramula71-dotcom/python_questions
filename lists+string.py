words = ["apple", "banana", "kiwi", "orange", "grape"]
new_lst=[]
for i in words:
    if len(i)>5:
        new_lst.append(i)
print(new_lst)