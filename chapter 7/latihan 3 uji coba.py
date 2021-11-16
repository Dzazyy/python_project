try:
    def tempat_file():
        global direkfile
        direkfile = input('masukan direktori file: ')
        
    
    def rata_ratanya():
        print('-----------------------------')
        print('PROGRAM HITUNG RATA-RATA')
        print('-----------------------------')
        file = open(direkfile , 'r+')
        angka = int(input('masukan Bilangan bulat yang mau ditambahkan:'))
        file.write(str(angka))
        while True:
            penanya = input('Mau lagi (y/n): ')
            if penanya == 'y':
                angka_t = int(input('Bilangan bulat yang mau ditambahkan:'))
                file.write('\n'+ str(angka_t))
            else:
                file.close()
                
                break

                         
    tempat_file()
    rata_ratanya()
    file = open(direkfile , 'r')
    sum = 0
    bagi = 0
    for data in file:
        bagi = bagi + 1
        sum = sum + int(data)
    rata = sum / bagi
    print ('rata-ratanya adalah ' + str(rata))
    
except FileNotFoundError:
    print('direktori file yang anda masukan tidak benar ')
    print('pastikan kali ini benar')
    tempat_file()
except ValueError:
    print('tidak boleh berupa huruf')
    print('pastikan kali ini benar')
    rata_ratanya()