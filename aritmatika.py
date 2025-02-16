print("---------------------------------")
print("| okhh time to aritmatika guiss |")
print("---------------------------------")

# operasi aritmatika = +, -, *, /
a = 4
b = 2

# operasi penjumlahan +
print("operasi penjumlahan")
hasil = a + b
print(a, "+", b, "=", hasil)
print("---------------------------------")

# operasi pengurangan -
print("operasi pengurangan")
hasil = a - b
print(a, "-", b, "=", hasil)
print("---------------------------------")

# operasi perkalian *
print("operasi perkalian")
hasil = a * b
print(a, "*", b, "=", hasil)
print("---------------------------------")

# operasi pembagian /
print("operasi pembagian")
hasil = a / b
print(a, "/", b, "=", hasil)
print("---------------------------------")

# operasi eksponen (pangkat) **
print("operasi eksponen")
hasil = a ** b
print(a, "**", b, "=", hasil)
print("---------------------------------")

# operasi modulus % (sisa bagi)
print("operasi modulus")
hasil = a % b
print(a, "%", b, "=", hasil)
print("---------------------------------")

# operasi floor division // kebalikan modulus (dibulatkan kebawah)
print("operasi floor division")
hasil = a // b
print(a, "//", b, "=", hasil)
print("---------------------------------")

print("prioritas operasi")

# prioritas operasi
# ()
# eksponen (pangkat)
# perkalian dan teman teman * / // %
# penjumlahan & pengurangan + _

x = 4
y = 2
z = 6

hasil = x ** y * z + x / y - y % z // x
print(x,"**",y,"*",z,"+",x,"/",y,"-",y,"%",z,"//",x,"=", hasil) 

hasil = x * y + z
print(x,"*",y,"+",z,"=", hasil)

hasil = (z - y) * x
print((z - y),"*",x,"=", hasil)