#Create a file containing a paragraph. Use read() to count the total number of words.
file=open("paragraph.txt","w")
file.write("Python can be used on a server to create web applications.\n"
"Python can be used alongside software to create workflows.\n""Python can connect to database systems. It can also read and modify files.\n""Python can be used to handle big data and perform complex mathematics.\n""Python can be used for rapid prototyping, or for production-ready software development.")
file.close()
file=open("paragraph.txt","r")
content=file.read()
word=content.split()
print(content)
print("no.of.words:",len(word))