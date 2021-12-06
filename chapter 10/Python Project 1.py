filenomor = open('nomor.txt', 'r')
angka = filenomor.readlines()
genap = 0
ganjil = 0
for i in range(len(angka)):
    angka[i].replace('\n','')
    hitung = angka[i]
    if (int(hitung) % 2) == 0:
        genap += 1
    else:
        ganjil += 1
print('banyak bilangan ganjilnya adalah '+ str(ganjil))
print('banyak bilangan genapnya adalah '+ str(genap))

