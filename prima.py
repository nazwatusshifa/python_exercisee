print('='*40)
print('Cek Bilangan Prima')
print('='*40)

num = int(input('Masukkan bilangan: '))
flag = False
if num == 1:
    print(num,'adalah bukan bilangan prima')
elif num > 1:
    for i in range(2,num):
        if num % i == 0:
            flag = True
            break
if flag:
     print(num,'bukan bilangan prima')
else:
    print(num,'bilangan prima')
