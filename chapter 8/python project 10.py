buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
total = []
buahnya = input('nama buah yang dibeli : ')
perbuah = int(buah[buahnya])
banyaknya = int(input('Berapa Kg		   : '))
totalperbuah = perbuah*banyaknya
total.append(totalperbuah)
print('-------------------------------------------')
print('Total harga		: ' +str(sum(total)))

