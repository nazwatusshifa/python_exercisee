USERNAME = "azthushif@gmail.com"
PASSWORD = "12345678"

username = (input("Masukkan username: "))
password = (input("Masukkan password: "))

if username != USERNAME:
    print("username anda tidak tersedia")
elif username == USERNAME and password != PASSWORD:
    print("password anda salah masukan lagi")
else:
    print(f"Selamat datang welll {username}")