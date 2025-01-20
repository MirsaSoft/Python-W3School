# MODIFIKASI STRING

# Python memiliki seperangkat metode bawaan yang dapat anda gunakan pada string.

# HURUF BESAR 

# Metode ini upper() mengembalikan string dalam huruf besar :

a = "Hello, World!"
print(a.upper())

print("===========================")

# HURUF KECIL

# Metode ini lower() mengembalikan string dalam huruf kecil :

a = "Hello, World!"
print(a.lower())

print("===========================")

# HAPUS SPASI

# Whitespace adalah spasi sebelum dan/atau sesudah teks sebenarnya, dan sering kali anda ingin menghapus spasi ini.

# Metode ini strip() menghapus spasi apa pun dari awal atau akhir :

a = " Hello, World! "
print(a.strip())

print("===========================")

# GANTI STRING

# Metode ini replace() mengganti string dengan string lain :

a = "Hello, World!"
print(a.replace("H", "J"))

print("===========================")

# PISAHKAN STRING

# Metode ini split() mengembalikan daftar di mana teks di antara pemisah yang ditentukan menjadi item daftar.

# Metode ini split() membagi string menjadi sub-string jika menemukan contoh pemisah :

a = "Hello, World!"
print(a.split(", "))
