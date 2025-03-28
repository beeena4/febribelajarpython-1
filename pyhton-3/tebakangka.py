import random # import angka acak

angka_rahasia = random.randint(1, 50) # angka random 1-50 
tebakan = -1 # tebakan diatur ke -1 sebagai nilai awal agar tidak sama dengan angka_rahasia secara default
percobaan = 0 # percobaan dihitung untuk melacak berapa kali pengguna mencoba menebak

while tebakan != angka_rahasia:
    try: # cek kesalahan input, jika benar lanjut
        tebakan = int(input("Tebak angka (1-50): ")) # perbaikan (int)
        percobaan += 1 # Setiap kali pengguna memasukkan tebakan, jumlah percobaan bertambah 1

        if tebakan < angka_rahasia:
            print("Tebakan terlalu kecil!")
        elif tebakan > angka_rahasia:
            print("Tebakan terlalu besar!")
        else:
            print("Selamat! Anda menebak dengan benar dalam", percobaan, "percobaan")

    except ValueError: # jika input tidak valid
        print("input tidak valid")