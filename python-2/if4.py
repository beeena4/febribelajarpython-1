# sampel If Else 4, if4.py:
# 006_A_FEBRIANA

# setelah perbaikan
i = int(input("Masukkan bilangan: ")) # mengganti float dengan int

if i % 2 == 0:  # Cek apakah bilangan genap
    if i == 0:  
        print("angka 0")  # Jika i = 0, cetak "angka 0"
    else:
        print(i, "adalah bilangan genap")  # Jika bukan 0, berarti genap
else:
    print(i, "adalah bilangan ganjil")  # Jika tidak genap, berarti ganjil