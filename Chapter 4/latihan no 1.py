import math
jam_ambil = int(input('masukan nilai jam pada satuan jam pada saat mengambil mobil? '))
jam_ambilmenit = int(input('masukan nilai menit pada satuan menit pada saat mengambil mobil? '))
jam_kembali = int(input('masukan nilai jam pada satuan jam pada saat mengembalikan mobil? '))
jam_kembalimenit = int(input('masukan nilai menit pada satuan menit pada saat mengembalikan mobil? '))
total_menit = abs((jam_ambil - jam_kembali)*60) + jam_ambilmenit + jam_kembalimenit
if total_menit <= 720 :
    total_biaya = 200000
else:
    total_biaya = ((total_menit - 720 ) / 60 * 10000) + 200000
print('lama anda meminjam adalah '+ str(total_menit) + ' menit')
print('total biaya yang harus anda bayarkan adalah Rp '+ str(round(total_biaya)))
