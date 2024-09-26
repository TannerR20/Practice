def Armstrong(n):
    final = 0
    temp = n
    while (n//10 != 0):
        digit = n % 10
        final = final + (digit**3)
        n = n//10
        print()
    if final == temp:
        print ("not Armstrong") 
    else:
        print("Armstrong") 

number = input("what is the number? ")
Armstrong(int(number))


