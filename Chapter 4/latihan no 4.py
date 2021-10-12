import math
jaraka_b = 125
kecepatana_b = 62
waktua_b = int(jaraka_b/kecepatana_b)*60
istirahat_b = 45
jarakb_c = 256
kecepatanb_c = 70
waktub_c = int(jarakb_c/kecepatanb_c)*60
totalwaktumenit = waktua_b+istirahat_b+waktub_c
totalwaktujam = totalwaktumenit/60
waktudepan = math.floor(6+totalwaktujam)
waktubelakang = math.floor((6+totalwaktujam) % 1 /0.25*15)
print("waktu yang dibutuhkan pak amir dalam menit adalah " + str(totalwaktumenit))
print("waktu yang dibutuhkan pak amir dalam jam adalah " + str(math.floor(totalwaktujam) + totalwaktujam % 1 /0.25*15*0.01))
print("perkiraan waktu Pak amir sampai = " + str(waktudepan) + ':' +str(waktubelakang) )