print('='*40)
print('PROGRAM TABUNG')
print('='*40)

def tabung():

    PHI = 3.14
    t = float(input('masukkan tinggi\t: '))
    r = float(input('masukkan jari2\t: '))

    volume = lambda PHI,t,r: PHI * r * r * t
    lp = lambda PHI,t,r: 2 * PHI * r * (r + t)

    print('volume: ',volume(PHI,t,r), 'cm')
    print('lp: ',lp(PHI,t,r), 'cm')

tabung()
tabung()
tabung()