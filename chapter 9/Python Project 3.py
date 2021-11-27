def bintang(n):
    n = (n //2) + 1
    space = 2*n-1
    for i in range (n):
        print(('*'*(2*i+1)).center(space))
    rspace = 2*n-1
    for i in reversed(range (n-1)):
        print(('*'*(2*i+1)).center(rspace))
bintang(9)