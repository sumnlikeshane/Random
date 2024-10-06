n = 5

for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

print()

for i in range(n):
    for j in range(i,n):
        print("*",end=" ")
    print()

print()

for i in range(n):
    for j in range(i,n-1):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()

print()

for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()


print()

for i in range(n):
    for j in range(i    ):
        print(" ",end=" ")
    for j in range(i,n-1):
        print("*",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()

print()

for i in range(n+1):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(1,i):
        print("*",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()


for i in range(1,n):
    for j in range(i):
        print(" ",end=" ")
    for j in range(i,n-1):
        print("*",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()

print()

n = 5
for i in range(n):
    for j in range(i + 1):
        print("*", end=" ")
    for j in range(2 * (n - i - 1)):
        print(" ", end=" ")
    for j in range(i + 1):
        print("*", end=" ")
    print()

for i in range(n - 1, 0, -1):
    for j in range(i):
        print("*", end=" ")
    for j in range(2 * (n - i)):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    print()

print()

n = 5
for i in range(1, n+1):
    if i != n:
        for j in range(i):
            print("*", end="")
        for j in range((2*n-(2*i))-1):
            print(" ", end="")
        for j in range(i):
            print("*", end="")
        print()
    else:
        for j in range((2*i)-1):
            print("*", end='')
        print()

for i in range(n-1, -1, -1):
    for j in range(i):
        print("*", end="")
    for j in range((2*n-(2*i))-1):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()

n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

n = 10
for i in range(n+1):
    for j in range(i+1):
        if j == 0 or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

for i in range(n):
    for j in range(i,n):
        if j == i or j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print()

n = 10
for i in range(n):
    for j in range(i+1):
        if i == n-1 or j == 0 or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print()

for i in range(n):
    for j in range(i,n):
        if i == 0 or j == i or j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()



