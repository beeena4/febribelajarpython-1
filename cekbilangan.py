# program pengecekan bilangan ganjil atau genap

jumlah = int(input("Masukkan jumlah bilangan: "))  # perbaikan (int)

genap = 0 # inisialisasi variabel
ganjil = 0 # inisialisasi variabel

for i in range(1, jumlah + 1):  # range dimulai dari 1 hingga jumlah selesai
    bil = int(input("Masukkan bilangan ke-{i}: "))  # input bilangan ke-(i) yang ingin di cek
    
    if bil % 2 == 0 : # perbaikan (:)
        genap += 1  
        print(bil, "adalah bilangan genap")  
    else :
        ganjil += 1  
        print(bil, "adalah bilangan ganjil")  

# menampilkan hasil setelah semua bilangan diperiksa
print("\nHasil Perhitungan:")  # perbaikan (hapus for in j, karena akan menampilkan hasil yang berulang)
print("Bilangan Genap   :",genap)  
print("Bilangan Ganjil  :",ganjil)