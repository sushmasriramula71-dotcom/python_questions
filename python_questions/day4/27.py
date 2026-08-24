def isprime(num):
    if num<=0:
        return False
    else:
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                return False

        else:
            return True
print(isprime(97))