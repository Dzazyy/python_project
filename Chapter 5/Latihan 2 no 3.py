bil_bulat = 0
bil_ganjil = 0
for i in range(100):
    bil = i + 1
    if bil % 2 != 0:
        bil_bulat += 1
        bil_ganjil += bil
        print(bil)
print("Banyak bilangan ganjil = " + str(bil_bulat))
print("Jumlah bilangan ganjil = " + str(bil_ganjil))