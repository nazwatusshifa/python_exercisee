print('='*40)
print('PROGRAM JAJAR GENJANG')
print('='*40)

def jajargenjang():

    a = float(input('masukkan alas\t: '))
    l = float(input('masukkan lebar\t: '))
    t = float(input('masukkan tinngi\t: '))
    p = float(input('masukkan panjang\t: '))

    luas = lambda a,t: a * t
    keliling = lambda l,p: 2 * l + p

    print('luas: ',luas(a,t), 'cm')
    print('keliling: ',keliling(l,p), 'cm')

jajargenjang()
jajargenjang()
jajargenjang()