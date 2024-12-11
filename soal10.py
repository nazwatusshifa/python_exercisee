total = float(input("Total Harga Barang: "))
jumlah_diskon = total * 5 / 100
total_bayar = total - jumlah_diskon

print(f'Hasil Diskon: {jumlah_diskon}')
print(f'Total Bayar : {total_bayar}')