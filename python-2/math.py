#Contoh math.py 
# 006_A_FEBRIANA

import math 
r=float(input("jari-jari lingkaran = ")) 
luas=math.pi*r*r 
print ("Luas lingkaran =",luas)

# setelah perbaikan
import math
r = float(input("\nMasukkan jari-jari lingkaran (cm)= "))
luas = math.pi * (r ** 2)
print(f"Luas lingkaran = {luas:.2f} cm²")