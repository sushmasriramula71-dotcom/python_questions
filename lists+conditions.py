arr=[1,2,3,2,4,1,5]
count=0
for i in range(len(arr)):
    if arr.count(arr[i])>1:
        if arr.index(arr[i])==i:
            count+=1