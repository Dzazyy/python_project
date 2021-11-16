from random import randint
health = 3
score = 0
print('Selamat datang di quiz Matematika')
print('pilih tingkat kesulitan anda')
print('dengan memilih pada angka awal pada pilihan dibawah')
print('1. Level 1 (Penjumlahan)')
print('2. Level 2 (Pengurangan)')
print('3. Level 3 (Perkalian)')
print('4. Exit')

inputan = int(input ('masukan option anda '))
if (inputan > 4) or (inputan < 0) :
    print('maaf anda tidak dapat melanjutkan quiz')
    exit()
while True:
    y = randint(-100,100)
    x = randint(-100,100)
    if health == 0:
        print('game telah tamat')
        print('score anda adalah ' + str(score))
        break
    elif inputan == 1 :
        hitungan = input('hitunglah hasil dari ' + str(x) + ' + ' + str(y) + '?  ')
        jawaban = str(x + y)
        if hitungan == jawaban:
            print('selamat anda benar')
            score += 2
            print('score anda sekarang adalah ' + str(score))
        else:
            print('sayang sekali anda salah')
            print('jawaban yang benar adalah '+ jawaban )
            health -= 1
            print('nyawa anda sisa '+ str(health))
    elif inputan == 2 :
        hitungan = input('hitunglah hasil dari ' + str(x) + ' - ' + str(y) + '?  ')
        jawaban = str(x - y)
        if hitungan == jawaban:
            print('selamat anda benar')
            score += 2
            print('score anda sekarang adalah ' + str(score))
        else:
            print('sayang sekali anda salah')
            print('jawaban yang benar adalah '+ jawaban )
            health -= 1
            print('nyawa anda sisa '+ str(health))
    elif inputan == 3 :
        hitungan = input('hitunglah hasil dari ' + str(x) + ' X ' + str(y) + '?  ')
        jawaban = str(x * y)
        if hitungan == jawaban:
            print('selamat anda benar')
            score += 2
            print('score anda sekarang adalah ' + str(score))
        else:
            print('sayang sekali anda salah')
            print('jawaban yang benar adalah '+ jawaban )
            health -= 1
            print('nyawa anda sisa '+ str(health))
    elif inputan == 4 :
        print('anda telah mengundurkan diri dari permainan ini')
        exit()

