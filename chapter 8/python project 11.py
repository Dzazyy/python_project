lstangka = []
angka = int(input('berapa banyak angka yang ingin anda urutkan: '))
for n in range(angka):
    numbers = int(input('Enter number '))
    lstangka.append(numbers)
lstangka.sort(reverse=True)
print("urutan angkanya adalah :"+ str(lstangka))