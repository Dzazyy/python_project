from datetime import *
filenya = open('dataperpus.txt','w+')
isian = []
while True:
    kode = input('Masukkan Kode Member	: ')
    name = input('Masukkan Nama Member	: ')
    judul = input('Masukkan Judul Buku	: ')
    option = input('Ulangi lagi (y/n)	: ')
    gabung = kode + "|" + name + "|" + judul + "|"  + str(datetime.date(datetime.now())) + "|" + str((datetime.date(datetime.now()+timedelta(days=7))))
    isian.append(gabung)
    if option in ('n','N'):
        for i in range(len(isian)):
            filenya.write(str(isian[i]) + '\n')
        filenya.close()
        break