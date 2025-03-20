# hapus nilai dalam tuple
tup = ('USM', 'Jaya', 1988, 2019)

print ("Tuple sebelum dihapus : ", tup) 

# mengahpus tuple
del tup

# menampilkan hasil setelah dihapus menggunakan try except
try :
    print ("Setelah menghapus tuple: ", tup) 
except NameError:
     print ("Tuple telah dihapus, sehingga tidak dapat mengakses lagi") 

print("© by FEBRIANA_006") 