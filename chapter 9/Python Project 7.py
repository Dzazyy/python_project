print('==========================================================')
print('NIM'.ljust(10),end='')
print('NAMA MAHASISWA'.ljust(22),end='')
print('TGL LAHIR'.ljust(13),end='')
print('TEMPAT LAHIR'.ljust(14))
print('----------------------------------------------------------')
mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO', 
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']
nim = []
nama = []
tgl =[]
tglfix = []
tlair = []
for z in range(len(mhs)):
    x = mhs[z].split(':')
    nim.append(x[0])
    nama.append(x[1])
    tgl.append(x[2])
    tlair.append(x[3])
for i in range(len(tgl)):
    kx = tgl[i].split('-')
    fx = str(kx[2]) +'-'+ str(kx[1]) +'-'+ str(kx[0])
    tglfix.append(str(fx))
for l in range (len(nama)):
    print(nim [l].ljust(10),end='')
    print(nama[l].ljust(22),end='')
    print(tglfix[l].ljust(13),end='')
    print(tlair[l].ljust(14))
