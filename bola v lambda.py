print('='*40)
print('PROGRAM BOLA')
print('='*40)

def bola():

    PHI = 3.14 
    r = float(input('masukkan jari2\t: '))

    lp = lambda PHI,r: 4 * PHI * r * r
    v = lambda PHI,r: 4/3 * PHI * r * r * r

    print('lp : ',lp(PHI,r), 'cm')
    print('v : ',v(PHI,r), 'cm')

bola()
bola()
bola()