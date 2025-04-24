# Fungsi untuk mencari bunga berdasarkan nama
def cari_bunga(daftar_bunga, nama_dicari):
     # Iterasi (looping) setiap nama bunga dalam daftar
    for bunga in daftar_bunga:
        # Membandingkan nama bunga dengan input pengguna
        if bunga.lower() == nama_dicari.lower():
            return True  # Ditemukan, kembalikan nilai True
    return False  # Tidak ditemukan, kembalikan nilai False

# Daftar bunga yang tersedia di toko
daftar = ["Mawar", "Melati", "Tulip", "Anggrek", "Kamboja"]

# Meminta input dari pengguna untuk nama bunga yang ingin dicari
nama_input = input("Masukkan nama bunga yang ingin dicari : ")

# Mengecek apakah bunga ada dalam daftar dengan memanggil fungsi cari_bunga dan menampilkan hasil pencarian
if cari_bunga(daftar, nama_input):
    print(f"{nama_input} tersedia di toko.")  # Jika bunga ditemukan
else:
    print(f"{nama_input} tidak tersedia.")  # Jika bunga tidak ditemukan

# Menampilkan Identitas
print("by : Febriana N.A_006")