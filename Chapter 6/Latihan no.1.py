import math
def isPythagoras(a, b, c):
    a_sqrt = math.sqrt(c ** 2 - b ** 2)/a
    b_sqrt = math.sqrt(c ** 2 - a ** 2)/b
    c_sqrt = math.sqrt(a ** 2 + b ** 2)/c
    if a_sqrt == True or b_sqrt == True or c_sqrt == True:
        print('a = ' + str(a) + ',' + ' b = ' + str(b) + ',' + ' c = ' + str(c) + ' --> ' +'True')
    else:
        print('a = ' + str(a) + ',' + ' b = ' + str(b) + ',' + ' c = ' + str(c) + ' --> ' +'false')
isPythagoras(3, 4, 5)
isPythagoras(5, 9, 12) 
isPythagoras(8, 6, 10)
isPythagoras(7, 8, 11)