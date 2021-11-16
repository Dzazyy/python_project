from operator import itemgetter as i
nilaiMhs = [{'nim' : 'A01', 'nama' : 'Amir', 'mid' : 50, 'uas' : 80}, 	      
            {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90},       
            {'nim' : 'A03', 'nama' : 'Cici', 'mid' : 50, 'uas' : 50}, 
            {'nim' : 'A04', 'nama' : 'Dedi', 'mid' : 20, 'uas' : 30}, 
	        {'nim' : 'A05', 'nama' : 'Fifi', 'mid' : 70, 'uas' : 40}]
for z in range(len(nilaiMhs)):
    nilaiakhir = (nilaiMhs[z]['mid']+nilaiMhs[z]['uas']+nilaiMhs[z]['uas'])//3
    nilaiMhs[z]['nilai akhir'] = nilaiakhir
mylist = sorted(nilaiMhs, key=i('uas'),reverse= True)
print('nilai akhir tertinggi adalah nim '+ mylist[0]['nim'] + ' bernama ' + mylist[0]['nama'])
