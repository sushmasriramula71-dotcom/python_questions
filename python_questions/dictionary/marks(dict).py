marks={"A":60,"B":75,"C":56}
lar=0
for m in marks.values():
    if lar<m:
        lar=m

print(lar)
