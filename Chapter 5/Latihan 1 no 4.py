def gaji(kode,nama,golongan):
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
  print('Potongan ('+ str(potongan*100) + '%)		: Rp ' + str(gaji_pokok * potongan))
  print ('----------------------------------------------------------- - ')
  print('Gaji Bersih			: ' + str(gaji_pokok - (gaji_pokok * potongan)))
gaji(input('Masukkan kode karyawan	: ') , input('Masukkan nama karyawan	: ') , input('Masukkan golongan          : '))
