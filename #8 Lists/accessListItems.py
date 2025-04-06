# AKSES ITEM

# Item daftar diindeks dan anda dapat mengaksesnya dengan merujuk ke nomor indeks :

thislist = ["apple", "banana", "cherry"]
print(thislist[1])

print("===========================")

# PENGINDEKSAN NEGATIF

# Pengindeksan negatif berarti mulai dari akhir. -1 merujuk pada item terakhir, -2 merujuk pada item kedua terakhir, dst.

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

print("===========================")

# RENTANG INDEKS

# Anda dapat menentukan rentang indeks dengan menentukan di mana memulai dan di mana mengakhiri rentang tersebut.

# Saat menentukan rentang, nilai yang dikembalikan akan berupa daftar baru dengan item yang ditentukan.

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

print("===========================")

# Dengan menghilangkan nilai awal, rentang akan dimulai pada item pertama :

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

print("===========================")

# Dengan menghilangkan nilai akhir, rentang akan berlanjutan hingga akhir daftar :

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

print("===========================")

# RENTANG INDEKS NEGATIF

# Tentukan indeks negatif jika anda ingin memulai pencarian dari akhir daftar :

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

print("===========================")

# PERIKSA APAKAH ITEM ADA

# Untuk menentukan apakah suatu item tertentu ada dalam suatu daftar, gunakan in kata kunci :

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")