print("="*40)
print("PROGRAM GEOMETRI KERUCUT")
print("="*40)

PHI = 3.14
r = float(input("Masukkan jari-jari: "))
s = float(input("Masukkan sisi: "))
t = float(input("Masukkan tinggi: "))

ls = PHI * r * s
lp = PHI * r * (r + s)
v = 1/3 * PHI * r * r * t

print(f"ls: ",ls, "cm")
print(f"lp: ",lp, "cm")
print(f"v: ",v, "cm")