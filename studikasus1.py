print("===================================")
print("        KALKULATOR SEDERHANA       ")
print("===================================")

def kalkulator():
    print("Operasi yang tersedia : ")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")

    pilihan = input("\nPilih Operasi (1/2/3/4) : ")
    print("-----------------------------------")
    angka1 = float(input("Masukkan angka pertama  : "))
    angka2 = float(input("Masukkan angka kedua    : "))

    if pilihan == '1':
        hasil = angka1 + angka2
    elif pilihan == '2':
        hasil = angka1 - angka2
    elif pilihan == '3':
        hasil = angka1 * angka2
    elif pilihan == '4':
        hasil = angka1 / angka2
    else:
        print("-----------------------------------")
        print("[ERROR] | Pilihan tidak valid")
        return
    print("-----------------------------------")
    print("Hasil : " , hasil)

kalkulator()