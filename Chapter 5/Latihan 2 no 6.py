from random import randint
jawaban = randint(0, 100)
poin =100
print('                  hallo selamat datang di permainan tebak angka                    ')
print('         di sini anda akan ditantang untung menebak angka dari 0 hingga 100        ')
print('perlu di ingat di sini pada mulanya anda punya 100 poin dan setiap salah akan berkurang 2')

while True:
    tebakan = input("Masukkan angka : ")
    if (int(tebakan) < jawaban ):
        print('  ')
        print("Terlalu kecil coba dibesarkan lagi angkanya")
        print('poin anda berkurang 2 sekarang tinggal '+ str(poin - 2) )
        print('  ')
        poin -= 2

    if (int(tebakan) > jawaban ):
        print('  ')
        print("Terlalu Besar coba dikecilkan lagi angkanya")
        print('poin anda berkurang 2 sekarang tinggal'+ str(poin - 2) )
        print('  ')
        poin -= 2
        
    if poin == 0 :
        print('kesempatan anda telah habis')
        print('anda tidak dapat menjawab lagi')
        break

    if (int(tebakan) == jawaban ):
        print("-------------------------------------------------------------------------------")
        print("Congratulation!!!! anda berhasil menebaknya !!!!")
        print("anda mendapatkan poin sebesar " + str(poin))
        print("Horeee anda telah berhasil menebaknya")
        break