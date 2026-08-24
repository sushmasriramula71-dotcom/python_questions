sentence=input("Enter a sentence").split(" ")
longest_word=""
for i in sentence:
    if len(i)>len(longest):
        longest=i
print(longest_word)
