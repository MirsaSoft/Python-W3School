# Built-in Data Types

# Dalam pemrograman, tipe data merupakan konsep penting.

"""
Variabel dapat menyimpan data dengan tipe yang berbeda, dan tipe yang berbeda dapat melakukan hal yang berbeda.

Python memiliki tipe data bawaan berikut, dalam kategori berikut :

- Tipe teks : str
- Tipe Numerik : int, float, complex
- Jenis Urutan : list, tuple, range
- Jenis Pemetaan : dict
- Jenis Set : set, frozenset
- Tipe Boolean : bool
- Tipe Biner : bytes, bytearray, memoryview
- Tidak ada tipe : NoneType

"""
# MENDAPATKAN TIPE DATA

# Anda bisa mendapatkan tipe data objek apa pun dengan menggunakan type() fungsi :

# Cetak tipe data variabel x :

x = 5
print(type(x))

print("===========================")

# MENGATUR TIPE DATA

# Dalam Python, tipe data ditetapkan saat anda menetapkan nilai ke variabel :

x = "Hello World"
print(x)
print(type(x))

print("===========================")

x = 20
print(x)
print(type(x))

print("===========================")

x = 20.5
print(x)
print(type(x))

print("===========================")

x = 1j
print(x)
print(type(x))

print("===========================")

x = ["apple", "banana", "cherry"]
print(x)
print(type(x))

print("===========================")

x = ("apple", "banana", "cherry")
print(x)
print(type(x))

print("===========================")

x = range(6)
print(x)
print(type(x))

print("===========================")

x = {"name" : "John", "age" : 36}
print(x)
print(type(x))

print("===========================")

x = {"apple", "banana", "cherry"}
print(x)
print(type(x))

print("===========================")

x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))

print("===========================")

x = True
print(x)
print(type(x))

print("===========================")

x = b"Hello"
print(x)
print(type(x))

print("===========================")

x = bytearray(5)
print(x)
print(type(x))

print("===========================")

x = memoryview(bytes(5))
print(x)
print(type(x))

print("===========================")

x = None
print(x)
print(type(x))

print("===========================")
