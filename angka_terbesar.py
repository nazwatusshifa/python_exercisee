import random
import 

n1 = int(input('Masukkan angka pertama: '))
n2 = int(input('Masukkan angka kedua: '))
step = int(input('Jumlah angka dalam deretnya: '))
deret = []
for i in range(0,step):
    i = random.randint(n1,n2)
    deret.append(i)
    max = max(deret)

print(f'Deret kamu adalah{deret}')
print(f'Angka terbesar dalam deret kamu adalah: {max}')
