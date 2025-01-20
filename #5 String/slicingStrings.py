# SLICING

# Anda dapat mengembalikan serangkaian karakter dengan menggunakan sintaksis irisan. Tentukan indeks awal dan indeks akhir, dipisahkan dengan titik dua, untuk mengembalikan bagian string.

# Dapatkan karakter dari posisi 2 ke posisi 5 (tidak termasuk) :

b = "Hello, World!"
print(b[2:5])

print("===========================")

# IRISAN DARI AWAL

# Dengan menghilangkan indeks awal, rentang akan dimulai pada karakter pertama :

# Dapatkan karakter dari awal hingga posisi 5 (tidak termasuk) :

b = "Hello, World!"
print(b[:5])

print("===========================")

# POTONGAN SAMPAI AKHIR

# Dengan menghilangkan indeks akhir, rentangnya akan sampai ke akhir :

# Dapatkan karakter dari posisi 2, dan sampai akhir :

b = "Hello, World!"
print(b[2:])

print("===========================")

# PENGINDEKSAN NEGATIF

#  Gunakan indeks negatif untuk melalui irisan dari akhir string :

# Dapatkan karakternya :
# Dari : "o" di "Dunia!" (posisi -5)
# Kepada, tetapi tidak termasuk : "d" di "Dunia!" (posisi -2) :

b = "Hello, World!"
print(b[-5:-2])