pin = "nimda123"

print("_"*40)
print("Verifikasi Login Anda")
print("_"*40)

username = input("Masukkan Username Anda: ")
password = input("Masukkan Password Anda: ")

if password == pin:
    print("Login Berhasil")
else: 
    print("Salah, silahkan masukkan lagi")