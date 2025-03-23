#Contoh cara menghapus pada Dictionary Python 
dict = {'nama': 'udin', 'usia': 23, 'Class': 'Awal'} 

print("dict sebelum di hapus : ", dict)

del dict['nama'] # hapus entri dengan key 'Nama' 
dict.clear () # hapus semua entri di dict 
del dict # hapus dictionary yang sudah ada 

print ("dict['Usia']  : ", dict['usia']) 
print ("dict['School']: ", dict['School'])

print ("© by FEBRIANA_006") 