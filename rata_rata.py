print("="*40)
print("\t\tInputan Jumlah Perkalian Dengan Rata-Ratanya")
print("="*40)

n = int(input("\tMasukkan jumlah nilai yang ingin dijumlah: "))
total = 0

for i in range(n):
    nilai = int(input(f"\tMasukkan nilai ke {i+1}: "))
    total += nilai

rata_rata = total / n
print("\t","="*35)
print(f"\tjumlah total nilai: {round(total)}")
print(f"\tRata-rata nilai: {round(rata_rata)}")