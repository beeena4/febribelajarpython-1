# contoh 1, whileIf.py
# 006_A_FEBRIANA

# setelah perbaikan
nama = "beeena4"
kunci = "meow"
a = 0

while a < 3:
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    if username == nama and password == kunci:
        print("Password benar, akses diberikan!")
        break
    elif username != nama and password != kunci:
        print("Username dan password salah!")
    elif username != nama:
        print("Username salah!")
    else:
        print("Password salah!")
    
    a += 1  # Naikkan a setiap kali percobaan salah

if a == 3:
    print("Anda telah gagal 3 kali!")