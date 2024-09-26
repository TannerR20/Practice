flag = True
def prime(n):
    if n == 1:
        return False
    for i in range (2,n,1):
        if n % i == 0:
            return False
    return True
number = input("what number would you like to know the prime of? ")

if prime(int(number)) == True:
    print("prime")
else:
    print("not prime")