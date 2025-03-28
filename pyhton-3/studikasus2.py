def cek_hari_kerja(hari):
    hari_kerja = ["senin", "selasa", "rabu", "kamis", "jumat"]

    if hari in hari_kerja:
        return "hari kerja"
    elif hari == "sabtu" or hari == "minggu":
        return "hari libur"
    else:
        return "hari tidak valid"
    
input_hari = input("Masukkan nama hari : ")
hasil = cek_hari_kerja(input_hari)
print(hasil)