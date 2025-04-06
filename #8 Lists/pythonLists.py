# DAFTAR

# Daftar digunakan untuk menyimpan beberapa item dalam satu variabel.

# Variabel adalah salah satu dari 4 tipe data bawaan dalam Python yang digunakan untuk menyimpan kumpulan data, 3 lainnya adalah Tuple, Set, dan Dictionary, semuanya dengan kualitas dan penggunaan yang berbeda.

# Daftar dibuat menggunakan tanda kurung siku :

thislist = ["apple", "banana", "cherry"]
print(thislist)

print("===========================")

# DAFTAR ITEM

# Item dalam daftar diurutkan, dapat diubah, dan memperbolekkan nilai duplikat. Item dalam daftar diindeks, item pertama mempunya indeks [0], item kedua mempunyai indeks, [1] dan seterusnya.

# DIPERINTAHKAN

# Ketika kita mengatakan bahwa daftar diurutkan, artinya item-itemnya memiliki urutan yang pasti, dan urutan itu tidak akan berubah. Jika anda menambahkan item baru ke suatu daftar, item baru tersebut akan ditempatkan di akhir daftar.

# DAPAT DIUBAH

# Daftar tersebut dapat diubah, artinya kita dapat mengubah, menambah, dan menghapus item dalam daftar setelah daftar dibuah.

# IZINKAN DUPLIKAT

# Karena daftar diindeks, daftar dapat memiliki item dengan nilai yang sama :

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

print("===========================")

# PANJANG DAFTAR

# Untuk menentukan beberapa banyak item yang dimiliki suatu daftar, gunakan len() fungsi :

thislist = ["apple", "banana", "cherry"]
print(len(thislist))

print("===========================")

# ITEM DAFTAR - TIPE DATA

# Item daftar dapat berupa tipe data apa pun :

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1)
print(list2)
print(list3)

print("===========================")

# Suatu daftar dapat berisi berbagai tipe data :

list1 = ["abc", 34, True, 40, "male"]
print(list1)

print("===========================")

# JENIS

# Dari perspektif Python, daftar didefinisikan sebagai objek dengan tipe data 'daftar' :

mylist = ["apple", "banana", "cherry"]
print(type(mylist))

print("===========================")

# KONSTRUKTOR LIST

# Dimungkinkan juga untuk menggunakan konstruktor list() saat membuat daftar baru.

thislist = list(("apple", "banana", "cherry"))
print(thislist)
