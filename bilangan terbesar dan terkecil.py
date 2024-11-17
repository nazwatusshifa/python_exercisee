print("="*40)
print("MENENTUKAN BILANGAN TERBESAR DAN TERKECIL")
print("="*40)

x = int(input("Masukkan bilangan 1: "))
y = int(input("Masukkan bilangan 2: "))
z = int(input("Masukkan bilangan 3: "))

if x > y and x > z:
    print(f"Bilangan terbesarnya ini {x}")
elif y > x and y > z:
    print(f"Bilangan terbesarnya ini {y}")
elif z > x and z > y:
    print(f"Bilangan terbesarnya ini {z}")
else:
    print()
if x < y and x < z:
    print(f"Bilangan terkecilnya itu {x}")
elif y < x and y < z:
    print(f"Bilangan terkecilnya itu {y}")
elif z < x and z < y:
    print(f"Bilangan terkecilnya itu {z}")