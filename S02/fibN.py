def fibonacci(n):
    a = 0
    b = 0
    c = 1
    for i in range (1,n+1):
        a = b
        b = c
        c = a + b
    return c

print(fibonacci(0))