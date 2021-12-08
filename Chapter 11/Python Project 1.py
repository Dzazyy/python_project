from datetime import *
tglin = input('masukan tanggal dalam format string \'YYYY-MM-DD\':  ')

def diffDate(x):
    tgl = datetime.date(datetime.now())
    tanggalnya = x.split('-')
    tglfix = date(int(tanggalnya[0]),int(tanggalnya[1]),int(tanggalnya[2]))
    tglselisih = tgl - tglfix
    return tglselisih.days

print('selisih tanggal hari ini dengan yang di inputkan adalah  :  ' +str(diffDate(tglin)) + ' hari')

