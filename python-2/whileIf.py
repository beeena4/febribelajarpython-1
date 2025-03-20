# contoh 1, whileIf.py

nama = "beeena4"
kunci = "meow"
a=0
while a!=3 :
    username = input("masukkan username : ")
    password = input("masukkan password : ")
    if username == nama and password == kunci :
        print("password benar")
        break
    elif username == nama or password == kunci :
        print("user and password error")
    else:
        print("password salah")
        a=a+1
if a==3:
    print("sudah 3x input")