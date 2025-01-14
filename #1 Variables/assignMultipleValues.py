# SATU NILAI KE BEBERAPA VARIABEL
# Dan anda dapat menetapkan nilai yang sama ke beberapa variabel dalam satu baris :

x = y = z = "Orange"
print(x)
print(y)
print(z)

print("===========================")

# BONGKAR KOLEKSI
# Jika anda memiliki kumpulan nilai dalam bentuk daftar, tuple, dsb. Python memungkinkan anda untuk mengekstrak nilai ke dalam variabel. INi disebut unpacking.

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
