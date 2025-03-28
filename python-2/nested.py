# contoh penggunaan nested loop
# 006_A_FEBRIANA

# setelah perbaikan
i = 2
while i < 100:
    j = 2
    while j <= (i // j):
        if i % j == 0:
            break
        j += 1
    if j > (i // j): 
        print(i, "INFORMATIKA UNESA")
    i += 1  

print("Mari bergabung bersama INFORMATIKA UNESA...JAYA!")