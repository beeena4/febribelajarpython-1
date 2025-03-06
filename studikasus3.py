print("====================================================")
print("                    KONVERSI SUHU                   ")
print("====================================================")

def konversi_suhu():
    print("1. Konversi dari Celcius ke Fahrenheit")
    print("1. Konversi dari Fahrenheit ke Celcius")

    pilihan = input("\nPilih konversi (1/2) : ")
    print("====================================================")
    

    if pilihan == '1':
        celcius = float(input("Masukkan suhu dalam Celcius : "))
        fahrenheit = (celcius * 9/5) + 32
        print("Suhu dalam Fahrenheit       : ", fahrenheit)
    elif pilihan == '2':
        fahrenheit = float(input("Masukkan suhu dalam Fahrenheit : "))
        celcius = (fahrenheit - 32) * 5/9
        print("Suhu dalam Celcius             : ", celcius)
    else:
        print("[ERROR] | Pilihan tidak valid")
    
konversi_suhu()