# KELUARAN VARIABEL
# Fungsi Python print() sering digunakan untuk mengeluarkan variabel.

x = "Python is awesome"
print(x)

print("===========================")

# Dalam print() fungsi tersebut, Anda mengeluarkan beberapa variabel, dipisahkan dengan koma :

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
print(x + y + z)

print("===========================")

# untuk angka, + karakter tersebut berfungsi sebagai operator matematika :

x = 5
y = 10
print(x + y)
print(x, y)

print("===========================")

# Dalam print() fungsi tersebut, saat anda mencoba menggabungkan string dan angka dengan + operator, Python akan memberikan anda kesalahan :

# Cara terbaik untuk menampilkan beberapa variabel dalam print() fungsi adalah dengan memisahkannya dengan koma, yang bahkan mendukung tipe data yang berbeda :

x = 5
y = "John"
print(x, y)