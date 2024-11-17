print("="*40)
print("PROGRAM MENENTUKAN DISKON BELANJA")
print("="*40)

print("Kamu akan mendapatkan diskon sebesar 25% jika total belanja nya lebih dari 100 ribu")

harga = float(input("Masukan total belanja: "))
diskon = harga * 25 / 100
total_harga_diskon = harga - diskon

if harga >= 100:
    print(f"selamat kamu mendapatkan diskon sebesar = 25%")
    print(f"diskon kamu teh segini = {diskon}")
    print(f"ini teh total harga yang harus di bayar = {total_harga_diskon}")
elif harga < 100:
    print(f"maaf euy karena total belanja kamu segini = {harga}\n jadi kamu tidak mendapatkan diskon")
print("nuhun nya engke mampir dei")