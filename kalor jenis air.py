print(35*"\033[36m=")
print("\033[34mKALOR JENIS AIR")
print(35*"\033[36m=")

c = float(input("Masukkan kalor jenis zat (J/kg°C): "))
m = float(input("Masukan massa (kg): "))
t = float(input("Masukkan perubahan suhu (°C): "))

Q1 = m * c * t

print(f"Jumlah kalor yang diperlukan adalah: ",Q1)