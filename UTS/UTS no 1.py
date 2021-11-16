def opin(tahun):
    if ((tahun % 400) == 0) or (((tahun % 400) != 0) and (tahun % 100 != 0) and (tahun % 4) == 0)  :
        print ('Tahun ' + str(tahun) + ' Merupakan Tahun Kabisat')
    elif ((tahun % 400) != 0) and ((tahun % 100) == 0):
        print ('Tahun ' + str(tahun) + ' Bukan Merupakan Tahun Kabisat')   
    else:
        print ('Tahun ' + str(tahun) + ' Bukan Merupakan Tahun Kabisat')
opin(int(input('Masukan tahun yang ingin anda cek   : ')))