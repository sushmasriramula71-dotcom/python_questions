list3=[10, 20, 10, 30, 20, 40, 30]
lar_num=list3[0]
sec_num=list3[0]
for i in list3:
    if i>lar_num:
        sec_num=lar_num
        lar_num=i
    elif i!=lar_num and i>sec_num:
        sec_num=i
print(sec_num)