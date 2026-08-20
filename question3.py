s=input()
low=s.lower().split()
low.sort()
print(low[0])

w=input()
lower=w.lower().split()
fst=lower[0]
for word in lower:
    if word<fst:
        fst=word
print(fst)

a=1
list_a=[5,"six",a,8.2]
list_b=[1,list_a]
print(list_b)