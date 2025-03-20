print("===================================")
print("        OPERASI  PENJUMLAHAN       ")
print("===================================")

def jumlah (a, b):
    return a + b

angka_1 = int(input("Masukkan angka pertama : "))
angka_2 = int(input("Masukkan angka kedua   : "))

print("-----------------------------------")
hasil = jumlah(angka_1, angka_2)
print(f"Hasil {angka_1} + {angka_2} : {hasil}")