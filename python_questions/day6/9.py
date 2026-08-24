#Read a file containing names and print only names whose length is greater than 5.
file=open("names.txt","r")
for name in file:
    name=name.strip()
    if len(name)>5:
        print(name)
