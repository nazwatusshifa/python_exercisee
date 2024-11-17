print('='*40)
print('PROGRAM LINGKARAN')
print('='*40)

def lingkaran():

    r = float(input('masukkan jari2\t: '))

    luas = lambda r: 3.14 * r * r
    keliling = lambda r: 2 * 3.14 * r
    diameter = lambda r: 2 * r

    print('luas: ',luas(r), 'cm2')
    print('keliling: ',keliling(r), 'cm')
    print('diameter: ',diameter(r), 'cm')