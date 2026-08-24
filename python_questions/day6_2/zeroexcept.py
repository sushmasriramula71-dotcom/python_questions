
wei=int(input("wei:"))
hei=float(input("hei: "))

try:
    bmi=wei/(hei**2)
except ZeroDivisionError:
    print("you gave value as zero")
except ValueError:
    print("you entered invalid data")
else:
    print(bmi)
finally:
    print("done")