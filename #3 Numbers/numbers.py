import random

# PYTHON NUMBERS

"""
Ada tiga tipe numerik dalam Python :
- int
- float
- complex
Variabel bertipe numerik dibuat saat anda menetapkan nilai padanya :

"""
x = 1
y = 2.8
z = 1j

# Untuk memverifikasi jenis objek apa pun di Python, gunakan type() fungsi :

print(type(x))
print(type(y))
print(type(z))

print("===========================")

# Int

# Int, atau integer, adalah bilangan bulat, positif atau negatif, tanpa desimal, degnan panjang tidak terbatas.

# Bilangan bulat :

x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

print("===========================")

# Float

# Float, atau "angka titik mengambang" adalah angka, positif atau negatif, yang mengandung satu atau lebih desimal.

# Contoh :

x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

print("===========================")

# Float juga bisa berupa angka ilmiah dengan "e" untuk menunjukkan pangkat 10.

# Contoh :

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

print("===========================")

# Complex

# Angka kompleks ditulis dengan "j" sebagai bagian imajiner :

# Contoh :

x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

print("===========================")

# KONVERSI TIPE

# Anda dapat mengonversi dari satu tipe ke tipe lain dengan metode int(), float(), dan complex() :

# Konversi dari satu tipe ke tipe lainnya :

x = 1
y = 2.8
z = 1j

a = float(x)
b = int(y)
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

print("===========================")

# ANGKA ACAK

# Python tidak memiliki random() fungsi untuk membuat angka acak, tetapi Python memiliki modul bawaan yang disebut random yang dapat digunakan untuk membuat angka acak :

# Impor modul acak, dan tampilkan angka acak antara 1 dan 9 :

print(random.randrange(1, 10))
