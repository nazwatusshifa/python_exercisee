print('='*40)
print('PROGRAM LINGKARAN')
print('='*40)

def segitiga():

    s = float(input('masukkan sisi : '))
    a = float(input('masukkan alas : '))
    t = float(input('masukkan tinggi : '))

    luas = lambda a,t: 1/2 * a * t
    keliling = lambda s: 3 * s

    print('luas: ',luas(a,t), 'cm')
    print('keliling: ',keliling(s), 'cm')

segitiga()
segitiga()
segitiga()