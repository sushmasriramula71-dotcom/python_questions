#Create a file containing 5 names. Use readlines() to read all names and print them one by one.
file=open("names.txt","w")
file.write("Sushma\nsusha\nsushil\nsushanth\nsushmitha\n")
file=open("names.txt","r")
cont=file.readlines()
for i in cont:
    print(i.strip())
# print(cont)