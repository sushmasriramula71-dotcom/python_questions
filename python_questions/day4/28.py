def max_num(nums):
    lar=nums[0]
    for i in nums:
        if i>lar:
            lar=i
    return lar
print(max_num([2,3,9,6,7,45,78,1,3]))