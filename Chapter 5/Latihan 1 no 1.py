nilai_indo = int(input('Masukkan nilai Bhs Indonesia     : '))
nilai_ipa  = int(input('Masukkan nilai IPA               : '))
nilai_mat  = int(input('Masukkan nilai Matematika        : '))


if nilai_indo >=0 and nilai_indo <=100 and nilai_ipa >=0 and nilai_ipa <=100 and nilai_mat >=0 and nilai_mat <=100:
    if nilai_indo > 60 and nilai_ipa > 60 and nilai_mat >70:
        Status = 'LULUS'
        print('Status Kelulusan		    : ' + Status)
    elif nilai_indo < 60 or nilai_ipa < 60 or nilai_mat <70:
        Status = 'TIDAK LULUS'
        print('Status Kelulusan		 : ' + Status)
else:
    print('Maaf input ada yang tidak valid')

if nilai_indo < 60 or nilai_ipa < 60 or nilai_mat <70:
    print ('Sebab        : ')
    if nilai_indo < 60:
        print('-	Nilai bahasa indonesia kurang dari 60' )
    if nilai_ipa < 60:
        print('-	Nilai ipa kurang dari 60' )
    if nilai_mat <70:
        print('-	Nilai Matematika kurang dari 70' )