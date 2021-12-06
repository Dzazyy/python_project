filenya = open('datamahasiswa.txt','w')
while True:
    nim = input('Masukkan NIM      : ')
    nama = input('Masukkan Nama     : ')
    alamat = input('Masukkan Alamat   : ')

    filenya.write(nim + '|' + nama + '|' + alamat + '\n')
    filenya.flush()
    pilihan = input('ingin memasukan data mahasiswa lagi y/n : ')
    if pilihan in ('N','n'):
        filenya.close()
        break