def fibonacci(n):
    a = 0
    b = 0
    c = 1
    for i in range (1,n+1):
        print(c)
        a = b
        b = c
        c = a + b
fibonacci(6)