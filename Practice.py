counter = 1
x=[1]
while counter != 10:
    print("#", end=" ")
    print( *x, sep=' ')
    x.insert(0,counter+1)
    counter+=1    

#another way
list =[]
for i in range(1,10):
    list.insert(0,i)
    print("#", ' '.join(map(str,list)))

def pyramid(n):
    for i in range (1, n+1):
        print("# ", end="")
        for j in range(i,0,-1):
            print(j,end=" ")
        print()
pyramid(10)