print("="*40)
print("|Program Kalender|")
print("="*40)

import calendar

tahun = int(input("Masukkan Tahun: "))
bulan = int(input("Masukkan Bulan: "))
print()

print("Hasil:")
print(calendar.month(tahun, bulan))