print('='*40)
print('PROGRAM TRAPESIUM')
print('='*40)

def trapesium():

    a = float(input('masukkan nilai a\t: '))
    b = float(input('masukkan nilai b\t: '))
    c = float(input('masukkan nilai c\t: '))
    d = float(input('masukkan nilai d\t: '))
    t = float(input('masukkan tinggi\t: '))

    luas = lambda a,b,t: 1/2 * (a + b) * t
    keliling = lambda a,b,c,d: a + b + c + d

    print('luas : ',luas(a,b,t), 'cm')
    print('keliling : ',keliling(a,b,c,d), 'cm')

trapesium()
trapesium()
trapesium()