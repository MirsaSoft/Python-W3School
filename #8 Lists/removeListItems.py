# HAPUS ITEM TERTENTU
# Metode ini remove() menghapus item yang ditentukan.

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
print("===========================")

# Jika ada lebih dari satu item dengan nilai yang ditentukan, remove() metode ini menghapus kemunculan pertama :

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)
print("===========================")

# HAPUS INDEKS TERTENTU
# Metode ini pop() menghapus indeks yang ditentukan.

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
print("===========================")

# Jika anda tidak menentukan indeks, pop() metode akan menghapus item terakhir.

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
print("===========================")

# Kata del kunci juga menghapus indeks yang ditentukan :

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
print("===========================")

# Kata del kunci juga dapat menghapus daftar sepenuhnya.

thislist = ["apple", "banana", "cherry"]
del thislist
print("===========================")

# HAPUS DAFTAR
# Metode ini clear() mengosongkan daftar. Daftarnya masih tetap ada, tetapi tidak ada isinya.

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
print("===========================")