# menampilkan judul aplikasi
print("---------------------------------------")
print(">>  Menghitung Luas Persegi Panjang  <<")
print("---------------------------------------")

# input panjang dan lebar dari pennguna
def hitung_luas_persegi_panjang():
    panjang = int(input("Masukkan Panjang : "))
    lebar = int(input("Masukkan Lebar   : "))

    if panjang == lebar:
        print("Yang anda masukkan bukan persegi panjang")
    else :
        luas = panjang * lebar
        print(f"Luas persegi panjang adalah : {luas}")
        print("---------------------------------------")

hitung_luas_persegi_panjang()