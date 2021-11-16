import math
#untuk permutasi
def P(n, r):
    f = math.factorial
    permutasi = f(n)//f(n-r)//1
    print('P : ' + str(permutasi))
P(10, 7)

#untuk combinasi
def C(n, r):
    f = math.factorial
    kombinasi = f(n)//f(r)//f(n-r)
    print('C : ' + str(kombinasi))
C(5, 3)