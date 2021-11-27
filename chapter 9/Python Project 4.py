import random
def randomkata(huruf,banyakkata):
    kata = []
    for i in range (banyakkata):
        hasil = ''.join(random.sample(huruf,len(huruf)))
        kata.append(hasil)
    print('randomkata(' + huruf +','+ str(banyakkata) + ') -> ' + str(kata))
x = input('masukan kata yang ingin diacak ')
y = int(input('masukan banyaknya urutan yang ingin diacak '))
randomkata(x,y)