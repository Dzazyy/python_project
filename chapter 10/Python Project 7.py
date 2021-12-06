penggeseran =  int(input('Masukan kode enkripsi anda: '))
filenya = open('dummywordenc.txt','r+')
dataMhs=[]
filekasar = filenya.readlines()
filementah = []
fileenkripsi = "" 
for i in range(len(filekasar)):
    datamurni = filekasar[i].replace('\n',' ')
    filementah.append(datamurni)
def chipper(text,s):
    hasil = ""
    for i in range(len(text)):
        if (ord(text[i])==32 ):
            hasil += ' '
        elif  (text[i].isupper()):
            hasil += chr((ord(text[i]) - s - 65) % 26 + 65)
        else:
            hasil += chr((ord(text[i]) - s - 97) % 26 + 97)
    return hasil
for i in range(len(filementah)): 
    fileenkripsi += chipper(filementah[i],penggeseran)

filedone = open('dummywordencback.txt','a+')
filedone.write(fileenkripsi)
filedone.close()