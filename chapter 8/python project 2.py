import copy
def dataStat(x):
    rata2 = copy.copy(x)
    i=0
    for f in range (len(rata2)):
        i += rata2[f]
    print('rata-ratanya adalah :' + str(i/len(rata2)))
    maks = copy.copy(x)  
    print('nilai tertingginya adalah: ' + str(max(maks)))
    minim =copy.copy(x)  
    print('nilai terendah dari list adalah: ' + str(min(minim)))

lstangka = []
angka = int(input('berapa banyak angka yang ingin anda urutkan: '))
for n in range(angka):
    numbers = int(input('Enter number '))
    lstangka.append(numbers)
dataStat(lstangka)