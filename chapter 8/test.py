a = [1, 5, 6, 3, 6, 9, 11, 20, 12] 
b = [7, 4, 5, 6, 7, 1, 12, 5, 9] 
c = a[0:7]
d = b[2:9]
totaldualist = zip(a ,b)
e = [x + y for (x,y) in totaldualist]
print (e)
cthtuple = tuple(e)
print(min(cthtuple))
print(max(cthtuple))
print(sum(cthtuple))
myString = ('python adalah bahasa pemrograman yang menyenangkan')
x = list(set(myString))
x.sort()
print(x)
