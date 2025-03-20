# Contoh 2: Fungsi dengan Pemanggilan Bersarang
# Fungsi untuk meminta input data dari pengguna
def input_data(): 
    """fungsi pertama"""
    nama = input("Masukan Nama :")  # Meminta input nama dari pengguna
    nim = input("Masukan NIM  :")  # Meminta input NIM dari pengguna

# Fungsi untuk mencetak pesan dan memanggil fungsi input_data
def cetak_string(): 
    print ("Ini adalah fungsi cetak string")  # Menampilkan pesan pertama
    print ("Silahkan masukan data")  # Menampilkan instruksi
    input_data()  # Memanggil fungsi input_data untuk meminta pengguna memasukkan data

# Memanggil fungsi cetak_string untuk menjalankan program
cetak_string()

print("© by FEBRIANA_006") 