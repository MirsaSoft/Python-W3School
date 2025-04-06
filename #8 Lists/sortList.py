# URUTAN DAFTAR BERDASARKAN ALFANUMERIK
# Objek daftar memiliki sort() metode yang akan mengurutkan daftar secara alfanumerik, menaik, secara default :

# Urutan daftar berdasarkan abjad :
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

print("===========================")

# Urutan daftar secara numerik

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

print("===========================")

# URUTAN SECARA MENURUN
# Untuk mengurutkan secara menurun, gunakan argumen kata kunci reverse = True :

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)
print(thislist)

print("===========================")

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

print("===========================")

# SESUAIKAN FUNGSI SORTIR
# Anda juga dapat menyesuaikan fungsi Anda sendiri dengan menggunakan argumen kata kunci. key = function
# Fungsi ini akan mengembalikan angka yang akan digunakan untuk emgnurutkan daftar (angka terendah terlebih dahulu) :

# Urutkan daftar berdasarkan seberapa dekat angka tersebut dengan 50 :
def myfunc(n):
    return abs(n - 50)

thislist = [ 100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

print("===========================")

# PENGURUTAN TANPA MEMBEDAKAN HURUF BESAR DAN KECIL
# Secara default, sort() metode ini peka huruf besar/kecil, sehingga semua huruf kapital akan diurutkan terlebih dahulu sebelum huruf kecil :

# Pengurutan peka huruf besar/kecil dapat memberikan hasil yang tidak diharapkan :
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

print("===========================")

# Untungnya kita dapat menggunakan fungsi bawaan sebagai fungsi utama saat mengurutkan daftar.
# Jadi jika Anda menginginkan fungsi pengurutan tanpa memperhatikan huruf besar/kecil gunakan str.lower sebagai fungsi kunci :

# Lakukan pengurutan daftar tanpa memperhatikan huruf besar/kecil :
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

print("===========================")

# URUTAN TERBALIK
# Bagaimana jika Anda ingin membalik susunan daftar, apapun abjadnya?
# Metode ini reverse() membalik susunan penyortiran elemen saat ini.

# Membalikkan urutan item daftar :
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)