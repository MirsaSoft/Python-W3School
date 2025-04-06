# TAMBAHKAN ITEM
# Untuk menambahkan item ke akhir daftar, gunakan metode append() :

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
print("===========================")

# MASUKKAN ITEM
# Untuk menyisipkan item daftar pada indeks tertentu, gunakan insert() metode. Metode ini insert() memasukkan item pada indeks yang ditentukan :

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
print("===========================")

# PERPANJANG DAFTAR
# Untuk menambahkan elemen dari daftar lain ke daftar saat ini, gunakan extend() metode.

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
print("===========================")

# TAMBAHKAN ITERABEL APAPUN
# Metode ini extend() tidak harus menambahkan daftar, anda dapat menambahkan objek apapun yang dapat diulang (tupel, set, kamus, dll.).

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
print("===========================")