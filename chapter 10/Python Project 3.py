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
print(dataMhs)
