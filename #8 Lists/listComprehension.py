# PEMAHAMAN DAFTAR
# Pemahaman daftar menawarkan sintaksis yang lebih pendek saat anda ingin membuat daftar baru berdasarkan nilai daftar yang ada.

# Contoh

# Berdasarkan daftar buah-buahan, anda menginginkan daftar baru yang hanya berisi buah-buahan dengan huruf "a" dalam namanya.
# Tanpa pemahaman daftar, anda harus menulis for pernyataan dengan pengujian kondisional di dalamnya :

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits :
    if "a" in x :
        newlist.append(x)
    
print(newlist)

print("===========================")

# Dengan pemahaman daftar, anda dapat melakukan semua itu hanya dengna satu baris kode :

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

print("===========================")

# SINTAKSIS
# Nilai yang dikembalikan adalah daftar baru, yang tidak mengubah daftar lama.

# KONDISI
# Kondisi ini seperti filter yang hanya menerima item yang bernilai True.

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)

print("===========================")

# Kondisi if x != "apple" akan kembali True untuk semua elemen selain "apel", membuat daftar baru berisi semua buah kecuali "apel".
# Kondisi ini bersifat opsional dan dapat dihilangkan :

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits]
print(newlist)

print("===========================")

# DAPAT DIULANG
# Yang dapat diulang dapat berupa objek apa saja, seperti daftar, tupel, set, dan sebagainya.

# Anda dapat menggunakan range() fungsi ini untuk membuat sesuatu yang dapat diulang :
newlist = [x for x in range(10)]
print(newlist)

print("===========================")

# Contoh yang sama, tetapi dengan suatu kondisi

# Terima hanya yang lebih rendah dari 5 :
newlist = [x for x in range(10) if x < 5]
print(newlist)

print("===========================")

# EKSPRESI
# Ekspresi adalah item saat ini dalam iterasi, tetapi juga merupakan hasil, yang dapat anda manipulasi sebelum berakhir seperti item daftar dalam daftar baru :

# Tetapkan nilai dalam daftar baru ke huruf besar :
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)

print("===========================")

# Anda dapat mengatur hasil sesuai keinginan anda :

# Tetapkan semua nilai dalam daftar baru ke "hello" :
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ['hello' for x in fruits]
print(newlist)

print("===========================")

# Ekspresi tersebut juga dapat berisi kondisi, bukan seperti filter, tetapi sebagai cara untuk memanipulasi hasilnya :

# Mengembalikan "orange" bukannya "banana" :
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)