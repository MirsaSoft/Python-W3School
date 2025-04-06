# GABUNGKAN DUA DAFTAR
# Ada beberapa cara untuk menggabungkan, atau menyatukan, dua atau lebih daftar dalam python.
# Salah satu cara termudah adalah dengan menggunakan + operator.

# Gabungkan dua list :
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

print("===========================")

# Cara lain untuk menggabungkan dua daftar dalah dengan menambahkan semua item dari list2 ke list1, satu persatu :

# Tambahkan list2 ke list1 :
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
for x in list2:
    list1.append(x)
    
print(list1)

print("===========================")

# Atau anda dapat menggunakan extend() metode ini, yang tujuannya adalah untuk menambahkan elemen dari satu daftar ke daftar lainnya :

# Gunakan extend() metode untuk menambahkan list2 di akhir list1 :
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)