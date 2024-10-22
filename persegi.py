print('='*40)
print('PROGRAM PERSEGI')
print('='*40)

def persegi():

    sisi = float(input('Masukkan sisi :'))

    keliling = lambda s: 4 * s
    ls = lambda s: s * s

    print('keliling : ',keliling(sisi), 'cm2')
    print('ls : ',ls(sisi), 'cm2')

persegi()
persegi()
persegi()