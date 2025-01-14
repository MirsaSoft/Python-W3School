# VARIABEL GLOBAL
# Variabel yang dibuat di luar suatu fungsi (seperti dalam semua contoh di halaman sebelumnya) dikenal sebagai variabel global.

# Variabel global dapat digunakan oleh siapa saja, baik di dalam fungsi maupun di luar.

# Buat variabel di luar fungsi dan gunakan di dalam fungsi

x = "awesome"

def myfunc() :
    print("Python is " + x)
    
myfunc()

print("===========================")

# Jika anda membuat variabel dengan nama yang sama di dalam suatu fungsi, variabel ini akan bersifat lokal, dan hanya dapat digunakan di dalam fungsi tersebut. Variabel global dengan nama yang sama akan tetap seperti sebelumnya, global dan dengan nilai aslinya.

# Buat variabel di dalam fungsi, dengan anma yang sama dengan variabel global

x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is " + x)
    
myfunc()
print("Python is " + x)

print("===========================")

# KATA KUNCI GLOBAL
# Biasanya, ketika anda membuat suatu variabel di dalam  suatu fungsi, variabel tersebut bersifat lokal, dan hanya dapat digunakan di dalam fungsi tersebut.

# Untuk membuat variabel global di dalam suatu fungsi, anda dapat menggunakan global kata kunci.

# Jika anda menggunakan global kata kunci, variabel tersebut termasuk dalam cakupan global :

def myfunc():
    global x
    x = "fantastic"
    
myfunc()

print("Python is " + x)

print("===========================")

# Gunakan juga global kata kunci jika ingin mengubah variabel global di dalam suatu fungsi.

# Untuk menggunakan nilai variabel global di dalam suatu fungsi, rujuk variabel tersebut dengan menggunakan global kata kunci :

y = "awesome"

def myfunc():
    global y
    y = "fantastic"
    
myfunc()

print("Python is " + y)