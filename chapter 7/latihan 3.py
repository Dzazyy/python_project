try:
    def menambah_baris_baru(tempat_file,textyangditambahkan):
        with open(tempat_file, 'a+') as barisbaru:
            while True:
                barisbaru.seek(0)
                data = barisbaru.read(100)
                if len(data) > 0:
                    barisbaru.write("\n")
                barisbaru.write(textyangditambahkan)
                penanya = input('Mau lagi (y/n): ')

                if penanya == 'y':
                    textyangditambahkan = input('Bilangan bulat yang mau ditambahkan:')
                else:
                    
                    hasil = open(tempat_file, 'r')
                    sum = 0
                    pembagi = 1
                    for data in hasil:
                        pembagi += 1
                        sum = sum + int(data)
                    print('bagi' + str(pembagi))
                    print('bagi' + str(pembagi))
                    hasil_bagi = sum / pembagi
                    print('Rata-ratanya adalah: ' + str(hasil_bagi))
                    break
    menambah_baris_baru(input('masukan direktori file: '),input('Bilangan bulat yang mau ditambahkan:'))        
except FileNotFoundError:
    print('direktori file yang anda masukan tidak benar')