



# try:
#     total=int(open("sources.txt").read())
# except FileNotFoundError:
#     print("file is not found")
# except ValueError:
#     print("file is not a number")
# else:
#     print(f"total is {total}")
# finally:
#     print("Done checking")



wei=int(input("wei:"))
hei=int(input("hei: "))

try:
    bmi=wei/(hei**2)
except ZeroDivisionError:
    print("you gave value as zero")
else:
    print(bmi)
finally:
    print("done")

