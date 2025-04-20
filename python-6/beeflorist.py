# Fungsi menampilkan Nama Toko
def tampilkan_namatoko():
    print("\n╔══════════════════════════════════════════════════════════════╗")
    print("║ +----------------------------------------------------------+ ║")
    print("║ | >>         << Selamat Datang di BEE Florist >>        << | ║")
    print("║ | >  Rangkai bunga terbaik untuk setiap moment spesial!  < | ║")
    print("║ +----------------------------------------------------------+ ║")
    print("╚══════════════════════════════════════════════════════════════╝")

# Data bunga
daftar_bunga = [
    {"no": 1, "nama": "Mawar", "harga": 15000, "stok": 10},
    {"no": 2, "nama": "Melati", "harga": 12000, "stok": 8},
    {"no": 3, "nama": "Tulip", "harga": 20000, "stok": 5},
    {"no": 4, "nama": "Anggrek", "harga": 18000, "stok": 7},
    {"no": 5, "nama": "Kamboja", "harga": 10000, "stok": 4}
]

# Fungsi menampilkan daftar bunga
def tampilkan_daftar():
    print("\nDaftar Bunga yang Tersedia:")
    print("=" * 64)
    print("| {:<2} | {:<28} | {:<16} | {:<5} |".format("No", "Nama Bunga", "Harga", "Stok"))
    print("|" + "-"*4 + "+" + "-"*30 + "+" + "-"*18 + "+" + "-"*7 + "|")
    
    for bunga in daftar_bunga:
        print("| {:<2} | {:<28} | Rp{:<14} | {:<5} |".format(
            bunga["no"], bunga["nama"], bunga["harga"], bunga["stok"]
        ))
    print("=" * 64)

# Fungsi pencarian bunga (linear search)
def cari_bunga(nama_dicari):
    for bunga in daftar_bunga:
        if bunga["nama"].lower() == nama_dicari.lower():
            return bunga
    return None

# Fungsi pembelian bunga
def beli_bunga():
    nama = input("\nMasukkan nama bunga yang ingin dibeli: ").strip()
    bunga = cari_bunga(nama)

    if bunga:
        print("Bunga Ditemukan:")
        print("===============================================================")
        print("| No  |       Nama Bunga         |       Harga       |  Stok  |")
        print("+-----+--------------------------+-------------------+--------+")
        print("| {:<3} | {:<24} | Rp{:<15} | {:<6} |".format
             (f"{bunga['no']}.", bunga["nama"], bunga["harga"], bunga["stok"]))
        print("===============================================================")
        try:
            jumlah = int(input("\nMasukkan jumlah yang ingin dibeli: "))
            if jumlah <= bunga["stok"]:
                total = jumlah * bunga["harga"]
                bunga["stok"] -= jumlah
                print("===============================================================")
                print("                     << STRUK PEMBELIAN >>                     ")
                print("===============================================================")
                print(f"Nama Bunga         : {bunga['nama']}")
                print(f"Harga Satuan       : Rp{bunga['harga']}")
                print(f"Jumlah Beli        : {jumlah}")
                print(f"Total Harga        : Rp{total}")
                print("===============================================================")
                print("Terima kasih telah berbelanja!")
            else:
                print("Stok tidak mencukupi!!.")
        except ValueError:
            print("Input tidak valid. Masukkan angka!!.\n")
    else:
        print("Bunga tidak ditemukan!!.\n")

# Menu utama
def menu():
    tampilkan_namatoko()  # Tampilan nama toko
    
    while True:
        print("\n================================================================")
        print("||>>                        M  E  N  U                      <<||")
        print("+ ============================================================ +")
        print("| 1. | Tampilkan Daftar Bunga                                  |")
        print("| 2. | Cari Bunga Berdasarkan Nama                             |")
        print("| 3. | Pesan Bunga                                             |")
        print("| 4. | Keluar                                                  |")
        print("================================================================")
        pilihan = input("Pilih menu (1-4): ")
        
        if pilihan == "1":
            tampilkan_daftar()
        elif pilihan == "2":
            nama = input("\nMasukkan nama bunga yang ingin dicari: ").strip()
            hasil = cari_bunga(nama)
            if hasil:
                print("Bunga Ditemukan:")
                print("===============================================================")
                print("| No  |       Nama Bunga         |       Harga       |  Stok  |")
                print("+-----+--------------------------+-------------------+--------+")
                print("| {:<3} | {:<24} | Rp{:<15} | {:<6} |".format(
                    f"{hasil['no']}.", hasil["nama"], hasil["harga"], hasil["stok"]
                ))
                print("===============================================================\n")
            else:
                print("Bunga tidak ditemukan!\n")
        elif pilihan == "3":
            beli_bunga()
        elif pilihan == "4":
            print("Terima kasih telah menggunakan aplikasi toko bunga!")
            break
        else:
            print("Menu belum tersedia atau pilihan tidak valid.")

# Jalankan aplikasi
menu()
