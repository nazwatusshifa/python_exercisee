print('='*40)
print('PROGRAM KERUCUT')
print('='*40)

def kerucut():

    PHI = 3.14
    r = float(input('masukkan jari2\t: '))
    s = float(input('masukkan sisi\t: '))
    t = float(input('masukkan tinggi\t: '))

    ls = lambda PHI,r,s: PHI * r * s
    lp = lambda PHI,r,s: PHI * r * (r + s)
    v = lambda PHI,r,t: 1/3 * PHI * r * r * t

    print('luas selimut : ',ls, 'cm')
    print('luas selimut : ',lp, 'cm')
    print('volume : ',v, 'cm')