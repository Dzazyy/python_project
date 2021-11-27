sayur = ['bayam', 'kangkung', 'wortel', 'selada']
while True:  
    def Tambahdatasayur():
        nama = str(input('Masukan nama sayur yang ingin anda tambah: '))
        sayur.append(nama)
        
    def hapusdatasayur():
        try:
            nama = input('Masukan nama sayur yang ingin anda Hapus: ')
            sayur.remove(nama)
        except ValueError:
            print('pastikan apa yang anda hapus terdapat di dalam list: ')
            print(sayur)
            hapusdatasayur()
    def Tampilkandatasayur():
        print(sayur)

    def jawab():
        print('pilih salah satu antara A/B/C')
        print('A.Tambah data sayur')
        print('B.Hapus data sayur')
        print('C.Tampilkan data sayur')
        print('D.keluar')
        pilihan = input('masukan option anda: ')
        if pilihan == 'A':
            Tambahdatasayur()
        elif pilihan == 'B':
            hapusdatasayur()
        elif pilihan == 'C':
            Tampilkandatasayur()
        else:
            break
    jawab()