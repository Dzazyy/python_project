lstname = []
nama = int(input('berapa banyak nama mahasiswa yang ingin anda urutkan: '))
for n in range(nama):
    name = str(input('Masukan nama  :'))
    lstname.append(name)
lstname.sort()
for i in range(len(lstname)):
    huruf = len(set(lstname[i]))
    print(lstname[i] + '(' + str(huruf) +' character ' + ')')