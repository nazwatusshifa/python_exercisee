print('='*40)
print('PROGRAM LIMAS SEGITIGA')
print('='*40)

def limassegitiga():

    la = float(input('masukkan luas alas : '))
    t = float(input('masukkan tinggi : '))

    v = lambda la,t: 1/3 * la * t

    print('v : ',v(la,t), 'cm')

limassegitiga()
limassegitiga()
limassegitiga()