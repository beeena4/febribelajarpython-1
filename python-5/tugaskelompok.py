class Stack: # Inisiasi class Stack
    def __init__(self, items=None): # Ini adalah fungsi konstruktor yang digunakan untuk menginisialisasi objek Stack.
        self.items = items if items is not None else [] # Jika argumen items tidak diberikan, maka self.items akan diinisialisasi sebagai list kosong.

    def is_empty(self): # Fungsi ini digunakan untuk memeriksa apakah stack kosong atau tidak.
        return len(self.items) == 0 # Jika self.items sama dengan 0, maka stack dianggap kosong.

    def push(self, item): # Fungsi ini digunakan untuk menambahkan item ke dalam stack.
        self.items.append(item) # Item baru ditambahkan ke akhir list self.items.

    def pop(self): # Fungsi ini digunakan untuk menghapus item dari stack.
        if not self.is_empty(): # Sebelum menghapus item, kita periksa apakah stack kosong.
            return self.items.pop() # Jika stack tidak kosong, item terakhir yang ditambahkan akan dihapus dan dikembalikan.

    def peek(self): # Fungsi ini digunakan untuk melihat item teratas dari stack tanpa menghapusnya.
        if not self.is_empty(): # Sebelum melihat item teratas, kita periksa apakah stack kosong.
            return self.items[-1] # Jika stack tidak kosong, item terakhir yang ditambahkan akan dikembalikan.

    def __repr__(self): # Fungsi ini digunakan untuk merepresentasikan objek Stack dalam bentuk string.
        return f"Stack({self.items})" # Fungsi ini digunakan untuk mengurutkan stack menggunakan stack tambahan.

def sort_stack(input_stack): # Fungsi ini digunakan untuk mengurutkan stack menggunakan stack tambahan.
    temp_stack = Stack() # Stack tambahan untuk menyimpan elemen sementara

    while not input_stack.is_empty(): # Selama stack input tidak kosong
        temp = input_stack.pop() # Ambil elemen teratas dari stack input

        while not temp_stack.is_empty() and temp_stack.peek() > temp: # Selama stack tambahan tidak kosong dan elemen teratas lebih besar dari elemen yang diambil
            input_stack.push(temp_stack.pop()) # Pindahkan elemen dari stack tambahan ke stack input

        temp_stack.push(temp) # Masukkan elemen yang diambil ke dalam stack tambahan

    while not temp_stack.is_empty(): # Setelah semua elemen dipindahkan ke stack tambahan
        input_stack.push(temp_stack.pop()) # Pindahkan elemen dari stack tambahan ke stack input

    input_stack.items.reverse() # Balikkan urutan stack input untuk mendapatkan urutan yang benar

    return input_stack # Menggunakan fungsi sort_stack untuk mengurutkan stack input


s = Stack([34, 3, 31, 98, 92, 23]) # Ini adalah input stack yang tidak terurut
print(f"Sebelum pengurutan: {s}") # Ini akan menampilkan stack input sebelum pengurutan
sorted_stack = sort_stack(s) # Menggunakan fungsi sort_stack untuk mengurutkan stack input
print(f"Setelah pengurutan: {sorted_stack}") # Ini akan menampilkan urutan stack Output: Stack([3, 23, 31, 34, 92, 98])