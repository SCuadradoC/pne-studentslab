def fibonacci(n):
    a = 0
    b = 0
    c = 1
    print(c) #this one is needed for f(0)
    for i in range (1,n+1):
        a = b
        b = c
        c = a + b
        print(c)

fibonacci(4)