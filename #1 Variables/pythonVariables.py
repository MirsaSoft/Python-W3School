# Variabel adalah wadah untuk menyimpan nilai data.

# MEMBUAT VARIABEL
# Python tidak memiliki perintah untuk mendeklarasikan variabel
# Suatu variabel tercipta pada saat pertama kali Anda menetapkan suatu nilai padanya.

x = 5
y = "John"
print(x)
print(y)

print("===========================")

# Variabel tidak perlu dideklarasikan dengan tipe tertentu, dan bahkan dapat mengubah tipe setelahnya ditetapkan.

x = 4
x = "Sally"
print(x)

print("===========================")

# CASTING
# Jika anda ingin menentukan tipe data suatu variabel, ini dapat dilakukan dengan casting.

x = str(3)
y = int(3)
z = float(3)
print(x)
print(y)
print(z)

print("===========================")

# GET THE TYPE
# Anda bisa mendapatkan tipe data suatu variabel dengan type() fungsi.

x = 5
y = "John"
print(type(x))
print(type(y))

print("===========================")

# TANDA KUTIP TUNGGAL DAN GANDA
# Variabel string dapat dideklarasikan dengan menggunakan tanda kutip tungga atau ganda :

x = "John"
print(x)
x = 'John'
print(x  )

print("===========================")

# CASE SENSITIVE
# Nama variabel peka huruf besar/kecil
a = 4
A = "Sally"
print(a)
print(A)
