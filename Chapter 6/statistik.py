def sum(*dataku):
    sum = 0
    for data in dataku:
        sum += data
    jumlah1 = sum
    print('jumlahnya :'+ str(jumlah1))
def average(*dataku):
    sum = 0
    t_angka=0
    for data in dataku:
        sum += data
        t_angka+=1
    ratarata = sum / t_angka
    print('rata-ratanya :'+ str(ratarata))
def mins(*dataku):

    for data in dataku:
        min(dataku) == data

    nilaiminimum1 = min(dataku)
    print('nilai minimum :'+ str(nilaiminimum1))
def maks(*dataku):

    for data in dataku:
        max(dataku) == data

    nilaiminimum1 = max(dataku)
    print('nilai minimum :'+ str(nilaiminimum1))
