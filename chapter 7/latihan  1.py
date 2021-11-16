try:
    direktori = input('masukan direktori file: ')
    tmpfile = open(direktori)
    print('isi dari ' + direktori + ' adalah: ')
    print(tmpfile.read())
except FileNotFoundError:
    print('direktori file yang anda masukan tidak benar')