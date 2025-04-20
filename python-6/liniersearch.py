def cari_bunga(daftar_bunga, nama_dicari):
    for bunga in daftar_bunga:
        if bunga.lower() == nama_dicari.lower():
            return True  # Ditemukan
    return False  # Tidak ditemukan

daftar = ["Mawar", "Melati", "Tulip", "Anggrek", "Kamboja"]
nama_input = input("Masukkan nama bunga yang ingin dicari : ")

if cari_bunga(daftar, nama_input):
    print(f"{nama_input} tersedia di toko.")
else:
    print(f"{nama_input} tidak tersedia.")
