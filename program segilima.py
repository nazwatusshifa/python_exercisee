print("="*40)
print("PROGRAM GEOMETRI SEGILIMA")
print("="*40)

s = float(input("Masukkan sisi: "))
l = float(input("Masukkan luas: "))
k = float(input("Masukkan keliling: "))
t = float(input("Masukkan tinggi: "))

luas = 5 * (s * t / 2)
keliling = 5 * s
tinggi = l / 5 * 2 / s
sisi = k / 5 or l / 5 * 2 / t

print("luas: ",luas, "cm")
print("keliling: ",keliling, "cm")
print("tinggi: ",tinggi, "cm")
print("sisi: ",sisi, "cm")