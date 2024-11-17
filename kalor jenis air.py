print(35*"\033[36m=")
print("\033[34mKALOR JENIS AIR")
print(35*"\033[36m=")

c = float(input("Masukkan kalor jenis zat (J/kg°C): "))
m = float(input("Masukan massa: "))
t = float(input("Masukkan perubahan suhu: "))

Q3 = m * c * t

print("Jumlah kalor yang diperlukan adalah: ",Q3)