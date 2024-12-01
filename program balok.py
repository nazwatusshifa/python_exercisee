print("="*40)
print("PROGRAM GEOMETRI BALOK")
print("="*40)

p = float(input("Masukkan panjang: "))
l = float(input("Masukkan lebar: "))
t = float(input("Masukkan tinggi: "))

v = p * l * t
lp = 2 * (p * l) + (p * t) + (l * t)

print(f"v : ",v, "cm")
print(f"lp : ",lp, "cm")