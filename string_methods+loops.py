s=input()
vowel_cnt=0
consnt_count=0
digits_count=0
for i in s:
    if i in "AEIOUaeiou":
        vowel_cnt+=1
    if i not in "AEIOUaeiou":
        consnt_count+=1
    if i.isdigit():
        digits_count+=1
print("Vowels: ",vowel_cnt)
print("Consonants: ",consnt_count)
print("Digits: ",digits_count)