from datetime import *
filenya = open('dataperpus.txt','r+')
isian = []
dataperpus = []
isinya = filenya.readlines()
for i in range(len(isinya)):
    datamurni = isinya[i].replace('\n','')
    isian.append(datamurni)
    splitkasar = isian[i].split('|')
    dictionary ={
        'kode' : splitkasar[0],
        'nama' : splitkasar[1],
        'judul' : splitkasar[2],
        'tglpinjam': splitkasar[3],
        'tglkembal': splitkasar[4]
    }
    dataperpus.append(dictionary)

def caridata(x):
    for zlk in range(len(dataperpus)):
        if x in str(dataperpus[zlk]):
            print('data mahasiswa di perpustakaan adalah:')
            print('kode             : ' + dataperpus[zlk]['kode'])
            print('nama             : ' + dataperpus[zlk]['nama'])
            print('judul            : ' + dataperpus[zlk]['judul'])
            print('tanggal pinjam   : ' + dataperpus[zlk]['tglpinjam'])
            print('tanggal Kembali  : ' + dataperpus[zlk]['tglkembal'])
            print('tanggal sekarang : ' + str(datetime.date(datetime.now())))
            tglnow =datetime.date(datetime.now())
            datback = dataperpus[zlk]['tglkembal']
            tanggalnya = datback.split('-')
            tglfix = date(int(tanggalnya[0]),int(tanggalnya[1]),int(tanggalnya[2]))
            tglselisih =  tglfix - tglnow
            if int(tglselisih.days) >= 0:
                print('Terlambat	  : - hari')
                print('Denda		  : Rp 0')
            elif int(tglselisih.days) < 0:
                print('Terlambat	  : '+ str(tglselisih.days*-1) +'hari')
                print('Denda		  : Rp '+ str((tglselisih.days*-1)*2000))
        if ((x in str(dataperpus)) == False):
            print('data tidak ditemukan')
datanya = input('masukan Kode Member	    : ')
caridata(datanya)


