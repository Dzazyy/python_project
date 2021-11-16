buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
total = []
def belibuah():
    while True:
        print(buah)
        buahnya = input('nama buah yang dibeli : ')
        perbuah = int(buah[buahnya])
        banyaknya = int(input('Berapa Kg   : '))
        totalperbuah = perbuah*banyaknya
        total.append(totalperbuah)
        pilihan = input('mau lagi Y/N    :')
        if pilihan == 'Y':
            continue
        else:
            break
    print('-------------------------------------------')
    print('Total harga		: ' +str(sum(total)))

def tambahbuah():
    while True:
        print(buah)
        nambuah = input('Masukkan nama buah 		: ')
        if nambuah == '':
            break
        if nambuah in buah:
            print('Nama Buah ' + str(nambuah) + ' harganya Rp. ' + str(buah[nambuah]))
        else:
            print('buah belum ada didalam daftar ')
            harbuah = int(input('Masukkan harga satuan		: '))
            buah[nambuah] = harbuah
            print('buah telah diupdate')

def hapusbuah():
    try:    
        nambuah = input('Masukkan nama buah 		: ')
        del buah[nambuah]
        print(buah)
    except KeyError:
        print('buah tidak ada silahkan coba lagi')
        hapusbuah()
print('Menu:\nA.	Tambah data buah\nB.	Beli buah\nC.	Hapus Buah')
option = input('masukan pilihan anda :')
if option == 'A':
    tambahbuah()
elif option == 'B':
    belibuah()
elif option == 'C':
    hapusbuah()
