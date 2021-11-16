buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
sortbuah = sorted(buah.items(), key=lambda x: x[1], reverse=True)
rata = []
for i in sortbuah:
	 rata.append(i[1])
rata2 = sum(rata)/len(rata)
print('hasil rata-rata satuanya adalah :' + str(rata2))
    