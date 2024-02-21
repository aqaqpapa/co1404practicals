for i in range(1, 21, 2):
    print(i, end=' ')
print()

#A
for i in range(0, 101, 10):
    print(i, end=' ')
print()

#B
for i in range(0,20,1):
    print(20-i,end=" ")
print()

#C
n=eval(input("Number of stars: "))
for i in range(1,n+1):
    print("*",end="")
print()
print("D")
for i in range(1,n+1):
    for o in range(1,i+1):
        print("*",end="")
    print()


