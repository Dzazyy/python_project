bil_bulat = 0
bil_ganjil = 0
while(bil_bulat <= 100):
    if(bil_bulat % 2 != 0):
        print(bil_bulat)
        bil_ganjil += 1
    bil_bulat += 1
print("Banyak Bilangan Ganjil : " + str(bil_ganjil))