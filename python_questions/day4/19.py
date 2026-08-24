tuple1=(10, 20, 10, 30, 10, 40, 20)
count_10=0
count_20=0
for i in tuple1:
    if i==10:
        count_10+=1
    if i==20:
        count_20+=1
print(f"occurance of 10 is {count_10} and occurance of 20 is {count_20}")