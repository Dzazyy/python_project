import math
jaraka_b = 125
jarakb_c = 256
kec1 = 62
kec2 = 70
lamawaktu1 = jaraka_b / kec1
lamawaktu2 = jarakb_c / kec2
jamdepan = math.floor( lamawaktu1 + lamawaktu2 + 0.75 )
jambelakang = ( lamawaktu1 + lamawaktu2 + 0.75) % 1 * 60
print(jambelakang)
print('pak Amir sampai di kota C pada pukul'+ str(jamdepan) + '.' +  str(jambelakang))