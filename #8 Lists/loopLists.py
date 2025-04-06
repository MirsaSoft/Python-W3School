# MELAKUKAN LOOPING MELALUI DAFTAR
# Anda dapat melakukan pengulangan melalui item-item dalam daftar dengan menggunakan for loop :

thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)
print("===========================")

# ULANGI MELALUI NOMOR INDEKS
# Anda juga dapat menelusuri item daftar dengan merujuk pada nomor indeksnya. Gunakan fungsi range() dan len() untuk membuat iterable yang sesuai.

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])
    
print("===========================")
    
# MENGGUNAKAN WHILE LOOP
# Anda dapat melakukan pengulangan pada item-item dalam daftar dengan menggunakan while perulangan
# Gunakan len() fungsi tersebut untuk menentukan panjang daftar, lalu mulai dari 0 dan lakukan pengulangan melalui item terdaftar dengan merujuk ke indeksnya.

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist) :
    print(thislist[i])
    i = i + 1
    
print("===========================")
    
# PERULANGAN MENGGUNAKAN PEMAHAMAN DAFTAR
# Pemahaman daftar menawarkan sintaksis terpendek untuk melakukan pengulangan melalui daftar :

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]