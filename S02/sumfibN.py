def sumfibN(n):
    a = 0
    b = 0
    c = 1
    tot = 1
    for i in range (1,n+1):
        a = b
        b = c
        c = a + b
        tot += c
    return tot

print(sumfibN(5),sumfibN(10))