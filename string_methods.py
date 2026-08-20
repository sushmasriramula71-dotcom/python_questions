#1
sen="Python is very easy to learn"
sen=sen.split(" ")
print(len(sen))

#2
sen="Python is very easy to learn"
sen=sen.upper()
print(sen)

#3
sen="Python is very easy to learn"
sen2=""
for i in sen.split():
    if i=="easy":
        sen2+="powerful "
        
    else:
        sen2+=i+" "
print(sen2)