print("="*40)
print("PROGRAM GEOMETRI TABUNG")
print("="*40)

PHI = 3.14
t = float(input("Masukkan tinggi: "))
r = float(input("Masukkan jari-jari: "))

v = PHI * r * r * t
lp = 2 * PHI * r * (r + t)

print(f"v: ",v, "cm")
print(f"lp: ",lp, "cm")