numbers=[10, 25, 30, 45, 50, 75, 90, 100]
new_list = []
for num in numbers:
    if num>30 and num%5==0 and num!=75:
        new_list.append(num)
print(new_list)