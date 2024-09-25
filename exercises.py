def swap(n1, n2):
    n1,n2=n2,n1
    print("n1 = ", n1)
    print("n2 = ", n2)

number1 = input("what is the first number? ")
number2 = input("what is the second number? ")
swap(number1, number2)

i=1
while (i< 10):   
    print(i)
    i+=1

#infinitely loops 4
    '''
quad = [1, 2, 3]
for i in quad:
    print(i)
    quad.append(4)
'''

for i in range (100, 200):
    if (i % 3 == 0 & i % 7 == 0):
        print("FooBar")
    elif (i % 3 == 0):
        print ("Foo")
    elif (i % 7 == 0):
        print("Bar")
flag = False
while (flag == False):
    digit = int(input("what is the number ?"))
    if (digit <= 0):
        flag = True
    elif ((digit) % 2 == 0):
        print("even")
    else:
        print("odd")

fib1= 0
fib2= 1
fib3 = fib2
while (fib2 < 100):
    print (fib1, end = ",")
    fib3 = fib1 + fib2
    fib1, fib2 = fib2, fib3
num1 = int(input("what is the number? "))
num2 = int(input("what is the second value? "))
def gcd(gcdnum1, gcdnum2):
    if (gcdnum1 == 0):
        print(gcdnum2)
    if (gcdnum2 == 0):
        print(gcdnum1)
    if (gcdnum1==gcdnum2):
        print (gcdnum1)
    if (gcdnum1 > gcdnum2):
            return gcd(a-b, b)
    return gcd(a, b-a)
