print('='*40)
print('PROGRAM BALOK')
print('='*40)

def balok():

    p = float(input('masukkan panjang\t: '))
    l = float(input('masukkan lebar\t: '))
    t = float(input('masukkan tinggi\t: '))

    v = lambda p,l,t: p * l * t
    lp = lambda p,l,t: 2 * (p * l) + (p * t) + (l * t)

    print('v : ',v(p,l,t), 'cm')
    print('lp : ',lp(p,l,t), 'cm')

balok()
balok()
balok()