# STRING

# String dalam python diapit oleh tanda kutip tunggal, atau tanda kutip ganda.

# 'halo' sama dengan "halo".

# Anda dapat menampilkan string literal dengan print() fungsi :

print("Hello")
print('Hello')

print("===========================")

# KUTIPAN DI DALAM KUTIPAN

# Anda dapat menggunakan tanda kutip di dalam string, selama tanda kutip tersebut tidak cocok dengan tanda kutip yang ada di sekitar string tersebut :

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

print("===========================")

# MENETAPKAN STRING KE VARIABEL

# Menetapkan string ke variabel dilakukan dengan nama variabel diikuti tanda sama dengan dan string :

a = "Hello"
print(a)

print("===========================")

# STRING MULTILINE

# Anda dapat menetapkan string multiline ke suatu variabel dengan menggunakan tiga tanda kutip :

a = """lorem ipsum dolor sit amet
consectetur adipiscing elit"""
print(a)

print("===========================")

# Atau tiga tanda kutip tebal

a = '''lorem ipsum dolor sit amet
consectetur adipiscing elit'''
print(a)

print("===========================")

# STRING ADALAH ARRAY

# Seperti banyak bahasa pemrograman populer lainnya, string dalam python adalah array byte yang mewakili karakter unicode.

# Akan tetapi, Python tidak memiliki tioe data karakter, karakter tunggal hanyalah string dengan panjang 1.

# Tanda kurung siku dapat digunakan untuk mengakses elemen string.

# Dapatkan karakter pada posisi 1 (ingat bahwa karakter pertama memiliki posisi 0) :

a = "Hello, World!"
print(a[1])

print("===========================")

# MELAKUKAN PERULANGAN MELALUI STRING

# Karena string adalah array, kita dapat melakukan pengulangan melalui karakter-karakter dalam string, dengan sebuah for pengulangan.

# Ulangi huruf-huruf dalam kata "banana" :

for x in "banana":
    print(x)
    
print("===========================")

# STRING LENGTH

# Untuk mendapatkan panjang string, gunakan len() fungsi>

# Fungsi ini len() mengembalikan panjang string :

a = "Hello, World!"
print(len(a))

print("===========================")

# CHECK STRING

# Untuk memeriksa apakah frasa atau karakter tertentu hadir dalam suatu string, kita dapat menggunakan kata kunci in

# Periksa apakah "gratis" ada dalam teks berikut :

txt = "The best things ini life are free!"
print("free" in txt)

print("===========================")

# Gunakan dalam sebuah if pernyataan :

# Cetak hanya jika ada "gratis" :

txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")
    
print("===========================")

# CHECK IF NOT

# Untuk memeriksa apakah frasa atau karakter tertentu tidak ada dalam suatu string, kita dapat menggunakan kata kunci not in.

# Periksa apakah "mahal" tidak ada dalam teks berikut :

txt = "The best things in life are free!"
print("expensive" not in txt)

print("===========================")

# Gunakan dalam sebuah if pernyataan :

# Cetak hanya jika "mahal" tidak ada :
txt = " The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")
    
