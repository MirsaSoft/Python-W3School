# UBAH NILAI ITEM

# Untuk mengubah nilai item tertentu, lihat nomor indeks :

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

print("===========================")

# MENGUBAH RENTANG NILAI ITEM

# Untuk mengubah nilai item dalam rentang tertentu, tentukan daftar dengan nilai baru, dan rujuk rentang nomor indeks tempat anda ingin memasukkan nilai baru :

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:1] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1] = ["blackcurrant", "watermelon"]
print(thislist)

print("===========================")

# Jika anda memasukkan item yang lebih sedikit daripada yang anda ganti, item baru akan dimasukkan di tempat yang anda tentukan, dan item yang tersisa akan dipindahkan sesuai dengan urutannya :

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

print("===========================")

# MASUKKAN ITEM

# Untuk menyisipkan item daftar baru, tanpa mengganti nilai apapun yang ada, kita dapat menggunakan insert() metode berikut. Metode ini insert() memasukkan item pada indeks yang ditentukan :

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)