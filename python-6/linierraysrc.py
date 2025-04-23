def cari_bunga_array(daftar_bunga, nama_dicari):
    for i in range(len(daftar_bunga)):
        if daftar_bunga[i][0].lower() == nama_dicari.lower():
            return daftar_bunga[i][1]  # Mengembalikan harga jika ditemukan
    return None  # Tidak ditemukan

# Daftar bunga: [nama, harga]
daftar = [
    ["Mawar", 15000],
    ["Melati", 12000],
    ["Tulip", 20000],
    ["Anggrek", 18000],
    ["Kamboja", 10000]
]

nama_input = input("Masukkan nama bunga yang ingin dicari : ")

harga = cari_bunga_array(daftar, nama_input)

if harga is not None:
    print(f"{nama_input} tersedia di toko dengan harga Rp{harga}.")
else:
    print(f"{nama_input} tidak tersedia.")
