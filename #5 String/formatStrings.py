# FORMAT STRING

# Seperti yang kita pelajari dibab Variabel Python, kita tidak dapat menggabungkan string dan angka seperti ini :

"""
age = 36
txt = "My name is John, I am " + age
print(txt)
"""

# Namun kita dapat menggabungkan string dan angka dengan menggunakan f-string atau format() metode ini !

# F-String

# F-String diperkenalkan dalam Python 3.6, dan sekarang menjadi cara yang disukai untuk memformat string.

# Untuk menentukan suatu string sebagai f-string, cukup letakkan sebuah f di depan literal string, dan tambahkan kurung kurawal {} sebagai tempat penampung untuk variabel dan operasi lainnya.

age = 36
txt = f"My name is John, I am {age}"
print(txt)

print("===========================")

# PLACEHOLDER DAN MODIFIER

# Placeholder dapat berisi variabel, operasi, fungsi, dan pengubah untuk memformat nilai.

# Tambahkan tempat penampung untuk price variabel :

price = 59
txt = f"The price is {price} dollars"
print(txt)

# Placeholder dapat menyertakan pengubahan untuk memformat nilai.

print("===========================")

# Pengubahan disertakan dengan menambahkan titik dua : diikuti oleh jenis format legal, seperti .2f yang berarti angka titik tetap dengan 2 desimal :

# Menampilkan harga dengan 2 desimal :

price = 59
txt = f"The price is {price:.3f} dollars"
print(txt)

print("===========================")

# Placeholder dapat berisi kode Python, seperti operasi matematika :

txt = f"The price is {20 * 59} dollars"
print(txt)

