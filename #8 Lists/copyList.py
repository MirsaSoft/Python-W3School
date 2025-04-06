# SALIN DAFTAR
# Anda tidak dapat menyalin daftar hanya dengan mengetik list2 = list1, karena : list2 hanyak akan menjadi referensi ke list1, dan perubahan yang dibuat dalam list1 akan secara otomatis juga dibuat dalam list2.

# GUNAKAN METODE copy()
# Anda dapat menggunakan metode daftar bawaan copy() untuk menyalin daftar.
# Buat salinan daftar dengan copy() metode :

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

print("===========================")

# GUNAKAN METODE list()
# Cara lain untuk membuat salinan dengan menggunakan metode bawaan list().

# Buat salinan daftar dengan list() metode :
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

print("===========================")

# GUNAKAN OPERATOR IRISAN
# Anda juga dapat membuat salinan daftar dengan menggunakan : operator (irisan).

# Buat salinan daftar dengan : operator :
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)