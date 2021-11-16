from random import randint
jawaban = randint(0, 100)

print('             hallo selamat datang di permainan tebak angka                    ')
print('     di sini anda akan ditantang untung menebak angka dari 0 hingga 100        ')

while True:
    tebakan = input("Masukkan angka : ")
    if (int(tebakan) < jawaban ):
        print('  ')
        print("Terlalu kecil coba dibesarkan lagi angkanya")
        print('  ')
    if (int(tebakan) > jawaban ):
        print('  ')
        print("Terlalu Besar coba dikecilkan lagi angkanya")
        print('  ')
    if (int(tebakan) == jawaban ):
        print("-------------------------------------------------------------------------------")
        print("Congratulation!!!! anda berhasil menebaknya !!!!")
        print("Horeee anda telah berhasil menebaknya")
        break