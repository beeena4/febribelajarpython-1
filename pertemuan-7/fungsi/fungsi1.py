# Contoh 1: Fungsi dan Pemanggilannya
# Fungsi untuk mencetak NIM dan Nama
def cetak_string(par1, par2): 
    print ("NIM Anda adalah  = ", par1)  # Menampilkan NIM yang dimasukkan
    print ("Nama Anda adalah = ", par2)  # Menampilkan Nama yang dimasukkan

# Fungsi untuk menghitung dan menampilkan hasil penjumlahan dua angka
def hitung(a, b): 
    print ("Hasil penjumlahan ", a, "+", b, "adalah", (a + b))  # Menampilkan hasil penjumlahan

# Program utama
nama = input("Masukan NIM Anda  = ")  # Meminta input dari pengguna untuk NIM
nim = input("Masukan Nama Anda  = ")  # Meminta input dari pengguna untuk Nama

# Memanggil fungsi cetak_string dengan parameter yang diperoleh dari input
cetak_string(nama, nim)

# Mendefinisikan dua bilangan
bill = 10  # Bilangan pertama
bil2 = 12  # Bilangan kedua

# Memanggil fungsi hitung untuk menjumlahkan dua bilangan
hitung(bill, bil2)

print("© by FEBRIANA_006") 