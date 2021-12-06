filenya = open('datamahasiswa.txt','r+')
dataMhs=[]
filekasar = filenya.readlines()
filementah = []
for i in range(len(filekasar)):
    datamurni = filekasar[i].replace('\n','')
    filementah.append(datamurni)
    splitkasar = filementah[i].split('|')
    dictionary ={
        'nim' : splitkasar[0],
        'nama' : splitkasar[1],
        'alamat' : splitkasar[2]
    }
    dataMhs.append(dictionary)
def caridata(x):
    for z in range(len(dataMhs)):
        if x in str(dataMhs[z]):
            print('data mahasiswanya adalah:')
            print('Nim    :' + dataMhs[z]['nim'])
            print('Nama   :' + dataMhs[z]['nama'])
            print('Alamat :' + dataMhs[z]['alamat'])
    if ((x in str(dataMhs)) == False):
        print('data tidak ditemukan')
datanya = input('masukan data yang ingin anda cari : ')
caridata(datanya)