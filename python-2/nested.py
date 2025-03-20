# contoh penggunaan nested loop
i = 2
while(i<100):
    j= 2
    while(j<= (i/j)):
        if not (i%j): break
        j = j + 1
    if (j > i/j): print(i, "AFF Learning")
    i= i + i
print("Mari bergabung bersama AFF Learning...AFF goOod learn!")