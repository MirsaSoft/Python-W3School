# NILAI BOOLEAN

# Dalam pemrograman anda sering kali perlu mengetahui apakah suatu ekspresi adalah true atau false. Saat anda membandingkan dua nilai, ekspresi dievaluasi dan Python mengembalikan jawaban boolean :

print(10 > 9)
print(10 == 9)
print(10 < 9)

print("===========================")

# Ketika anda menjalankan suatu kondisi dalam pernyataan if, Pyhton mengembalikan true atau false :

# Cetak pesan berdasarkan apakah kondisinya true atau false :

a = 200
b = 33

if b > a :
    print("b is greater than a")
else :
    print("b is not greater than a")
    
print("===========================")

# MENGEVALUASI NILAI DAN VARIABEL

# Fungsi ini bool() memungkinkan anda untuk mengevaluasi nilai apapun, dan memberi anda true atau false sebagai gantinya,

# Mengevaluasi string dan angka :

print(bool("Hello"))
print(bool(15))

print("===========================")

# Mengevaluasi dua variabel ;

x = "Hello"
y = 15
print(bool(x))
print(bool(y))

print("===========================")

# SEBAGIAN BESAR NILAI ADALAH BENAR

# Hampir semua nilai dievaluasi true apakah memiliki semacam konten. Semua string adalah true, kecuali string kosong. Setiap bilangan adalah true, kecuali 0. Semua daftar, tupel, himpunan, dan kamus adalah true, kecuali yang kosong.

# Berikut ini akan mengembalikan true :

print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

print("===========================")

# BEBERAPA NILAI SALAH

# Faktanya, tidak banyak nilai yang bernilai false, kecuali nilai kosong, seperti (), [], {}, "", angka 0, dan nilai None. Dan tentu saja nilainya false bernilai false.

# Berikut ini akan mengembalikan false :

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

print("===========================")

# Satu nilai lagi, atau objek dalam kasus ini, dievaluasi menjadi false, dan itu jika anda memiliki objek yang dibuat dari kelas dengan __len__ fungsi yang mengembalikan 0 atau false :

class myclass():
    def __len__(self):
        return 0
    
myobj = myclass()
print(bool(myobj))

print("===========================")

# FUNGSI DAPAT MENGEMBALIKAN BOOLEAN

# Anda dapat membuat fungsi yang mengembalikan nilai boolean :

# Cetak jawaban suatu fungsi :

def myFunction() :
    return True

print(myFunction())

# Anda dapat mengeksekusi kode berdasarkan jawaban boolean suatu fungsi :

# Cetak "YA!" jika fungsi mengembalikan benar, jika tidak cetak "TIDAK!" :

def myFunction() :
    return True

if myFunction() :
    print("YES!")
else :
    print("NO!")
    
print("===========================")

# Python juga memiliki banyak fungsi bawaan yang mengembalikan nilai boolean seperti isinstance() fungsi, yang dapat digunakan untuk menentukan apakah suatu objek memiliki tipe data tertentu :

# Periksa apakah suatu objek merupakan bilangan bulat atau bukan :

x = 200
print(isinstance(x, int))
