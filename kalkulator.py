# kalkulator sederhana
 
print("===================================")
print("        KALKULATOR SEDERHANA       ")
print("===================================")

angka_1 = float(input("Masukkan Angka 1 = "))
angka_2 = float(input("Masukkan Angka 2 = "))
operator = input("Masukkan Operator (+,-,x,/) = ")
print("-----------------------------------")

if operator == "+" :
    tambah = angka_1 + angka_2
    print(f"Hasil dari {angka_1} + {angka_2} = {tambah}")
elif operator == "-" :
    kurang = angka_1 - angka_2
    print(f"Hasil dari {angka_1} - {angka_2} = {kurang}")
elif operator == "x" :
    kali = angka_1 * angka_2
    print(f"Hasil dari {angka_1} x {angka_2} = {kali}")
elif operator == "/" :
    bagi = angka_1 / angka_2
    print(f"Hasil dari {angka_1} / {angka_2} = {bagi}")
else:
    print("Masukkan operator yang sudah ditentukan")