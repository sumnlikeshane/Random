n =5
def rec(n):
    if n==1:
        return 1
    else:
        return n*rec(n-1)

print(rec(5))