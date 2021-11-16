try:
    direktori = input('masukan direktori file: ')
    tmpfile = open(direktori,'a')
    while True :
        isitamb = input('Data yang mau ditambahkan:')
        tmpfile.write(isitamb) 
        penanya = input('Mau lagi (y/n): ')
        if penanya == 'y':
            continue
        else:
            tmpfile.close()
            break
except FileNotFoundError:
    print('direktori file yang anda masukan tidak benar')