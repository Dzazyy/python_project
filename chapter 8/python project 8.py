buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
sortbuah = sorted(buah.items(), key=lambda x: x[1], reverse=True)
for i in sortbuah:
	print(i[0], i[1])
