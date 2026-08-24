sentence = "Python is easy and Python is powerful"
list_sen=sentence.split(" ")
freq={}
for w in list_sen:
    if w not in freq:
        freq[w]=1
    else:
        freq[w]+=1
print(freq)