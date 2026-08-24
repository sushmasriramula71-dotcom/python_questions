# file=open("pratice2.py","w")
# file.write("from datetime import datetime\n"
# "date_today=datetime.now()\n"
# "print(date_today)")
# file.close()

# file=open("pratice2.py","r")
# content=file.read()
# print(content)
# exec(content)

# file=open("practice2.py","a")
# file.write("addded a new line")

# content=file.read()
# print(content)
# file.close()



try:
    total=int(open("sources.txt").read())
except FileNotFoundError:
    print("file is not found")
except ValueError:
    print("file is not a number")
else:
    print(f"total is {total}")
finally:
    print("Done checking")