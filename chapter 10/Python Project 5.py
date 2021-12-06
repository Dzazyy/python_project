filenya = open('Nomorkebawah.txt','r+')
data = filenya.readlines()
nomornya = []
print('hasil penjumlahanya adalah  :')
for i in range(len(data)):
    ubahan = data[i].replace('\n','')
    nomornya.append(ubahan)
    penjumlahan = nomornya[i].split('|')
    print(penjumlahan[0] + ' + ' + penjumlahan[1])
    print('=' + str(int(penjumlahan[0]) + int(penjumlahan[1])))
    