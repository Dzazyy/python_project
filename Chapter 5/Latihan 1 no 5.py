def gaji(kode,nama,golongan,kawin):
  if kawin == '1':
      jumlah_anak = int(input('Masukkan jumlah anak			: '))
  print ('      ')
  print ('====================================')
  print ('-----------------------------------------------------------')
  print ('Nama Karyawan		: ' + str(nama) + ' (Kode:' + str(kode) + ' )')
  print ('Golongan			: ' + str(golongan))
  print ('-----------------------------------------------------------')
  if golongan == 'A' :
      gaji_pokok = 10000000
  elif golongan == 'B'  :
      gaji_pokok = 8500000
  elif golongan ==  'C' :
      gaji_pokok = 7000000
  else :
      gaji_pokok = 5500000

  if golongan == 'A' :
      potongan = 0.025
  elif golongan == 'B'  :
      potongan = 0.02
  elif golongan ==  'C' :
      potongan = 0.015
  else :
      potongan = 0.01
  print('Gaji Pokok			: Rp ' + str(gaji_pokok))
  if kawin == '1':
      print("Tunjangan Menikah :" + "Rp " + str(gaji_pokok * 0.1))
      print("Tunjangan Anak    :" + "Rp " + str(jumlah_anak * 0.05 * gaji_pokok))
  print ('----------------------------------------------------------- + ')
  Gaji_kotor = gaji_pokok * 0.1 + jumlah_anak * 0.05 * gaji_pokok + gaji_pokok
  print('Gaji Kotor			: Rp ' + str(Gaji_kotor))
  print('Potongan ('+ str(potongan*100) + '%)		: Rp ' + str(Gaji_kotor * potongan))
  print ('----------------------------------------------------------- - ')
  print('Gaji Bersih			: ' + str(Gaji_kotor - (Gaji_kotor * potongan) ))
  print(kawin)
gaji(input('Masukkan kode karyawan	: ') , input('Masukkan nama karyawan	: ') , input('Masukkan golongan         : ') , input('Masukkan status (1: menikah, 2: blm)	:'))

