str=input("Enter a string")
vowel_count=0
for i in str:
    if i in "AEIOUaeiou":
        vowel_count+=1
print(vowel_count)