# OPERATOR PYTHON

# Operator digunakan untuk melakukan operasi pada variabel dan nilai. Dalam contoh di bawah ini, kami menggunakan + operator untuk menambahkan dua nilai :

print(10 + 5)

print("===========================")

"""
Python membagi operator ke dalam kelompok berikut :
- Operator aritmatika
- Operator penugasan
- Operator perbandingan
- Operator logika
- Operator identitas
- Operator keanggotaan
- Operator bitwise
"""

# OPERATOR ARITMATIKA PYTHON

# Operator aritmatika digunakan dengan nilai numerik untuk melakukan operasi matematika umum :

print(15 + 5) # Addition

print("===========================")

print(15 - 5) # Subtraction

print("===========================")

print(15 * 5) # Multiplication

print("===========================")

print(15 / 5) # Division

print("===========================")

print(15 % 5) # Modulus

print("===========================")

print(15 ** 5) # Exponentiation

print("===========================")

print(15 // 5) # Floor division

print("===========================")

# OPERATOR PENUGASAN
print("OPERATOR PENUGASAN")

x = 5
print(x)

print("===========================")

x = 15
x += 3
print(x)

print("===========================")

x = 15
x -= 3
print(x)

print("===========================")

x = 15
x *= 3
print(x)

print("===========================")

x = 15
x /= 3
print(x)

print("===========================")

x = 15
x %= 3
print(x)

print("===========================")

x = 15
x //= 3
print(x)

print("===========================")

x = 15
x **= 3
print(x)

print("===========================")

x = 15
x &= 3
print(x)

print("===========================")

x = 15
x |= 3
print(x)

print("===========================")

x = 15
x ^= 3
print(x)

print("===========================")

x = 15
x >>= 3
print(x)

print("===========================")

x = 15
x <<= 3
print(x)

print("===========================")

print(x := 3)

print("===========================")

# OPERATOR PERBANDINGAN

print("OPERATOR PERBANDINGAN")
x = 5
y = 3
print(x == y)

print("===========================")

x = 5
y = 3
print(x != y)

print("===========================")

x = 5
y = 3
print(x > y)

print("===========================")

x = 5
y = 3
print(x < y)

print("===========================")

x = 5
y = 3
print(x >= y)

print("===========================")

x = 5
y = 3
print(x <= y)

print("===========================")

# OPERATOR LOGIKA PYTHON

# Operator logika digunakan untuk menggabungkan pernyataan kondisional :

x = 5

print(x > 3 and x < 10) # and

print("===========================")

x = 5

print(x > 3 or x < 4)

print("===========================")

# OPERATOR IDENTITAS PYTHON

# Operator identitas digunakan untuk membandingkan objek, bukan jika objek tersebut sama, tetapi jika objek tersebut sebenarnya adalah objek yang sama, dengan lokasi memori yang sama :

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)

# returns True because z is the same object as x

print(x is y)

# returns False because x is not the same object as y, even if they have the same content

print(x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

print("===========================")

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is not z)

# returns False because z is the same object as x

print(x is not y)

# returns True because x is not the same object as y, even if they have the same content

print(x != y)

# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y

print("===========================")

# OPERATOR KEANGGOTAAN PYTHON

# Operator keanggotaan digunakan untuk menguji apakah suatu urutan disajikan dalam suatu objek :

x = ["apple", "banana"]

print("banana" in x)

# returns True because a sequence with the value "banana" is in the list

print("===========================")

x = ["apple", "banana"]

print("pineapple" not in x)

# returns True because a sequence with the value "pineapple" is not in the list

print("===========================")

# OPERATOR BITWISE PYTHON

# Operator bitwise digunakan untuk membandingkan angka (biner) :

print(6 & 3)



"""
The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
2 = 0000000000000010
====================

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
"""

print("===========================")

print(6 | 3)



"""
The | operator compares each bit and set it to 1 if one or both is 1, otherwise it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
7 = 0000000000000111
====================

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
"""

print("===========================")

print(6 ^ 3)



"""
The ^ operator compares each bit and set it to 1 if only one is 1, otherwise (if both are 1 or both are 0) it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
5 = 0000000000000101
====================

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
"""

print("===========================")

print(~3)



"""
The ~ operator inverts each bit (0 becomes 1 and 1 becomes 0).

Inverted 3 becomes -4:
 3 = 0000000000000011
-4 = 1111111111111100

Decimal numbers and their binary values:
 4 = 0000000000000100
 3 = 0000000000000011
 2 = 0000000000000010
 1 = 0000000000000001
 0 = 0000000000000000
-1 = 1111111111111111
-2 = 1111111111111110
-3 = 1111111111111101
-4 = 1111111111111100
"""

print("===========================")

print(3 << 2)



"""
The << operator inserts the specified number of 0's (in this case 2) from the right and let the same amount of leftmost bits fall off:

If you push 00 in from the left:
 3 = 0000000000000011
becomes
12 = 0000000000001100

Decimal numbers and their binary values:
 0 = 0000000000000000
 1 = 0000000000000001
 2 = 0000000000000010
 3 = 0000000000000011
 4 = 0000000000000100
 5 = 0000000000000101
 6 = 0000000000000110
 7 = 0000000000000111
 8 = 0000000000001000
 9 = 0000000000001001
10 = 0000000000001010
11 = 0000000000001011
12 = 0000000000001100
"""

print("===========================")

print(8 >> 2)



"""
The >> operator moves each bit the specified number of times to the right. Empty holes at the left are filled with 0's.

If you move each bit 2 times to the right, 8 becomes 2:
 8 = 0000000000001000
becomes
 2 = 0000000000000010

Decimal numbers and their binary values:
 0 = 0000000000000000
 1 = 0000000000000001
 2 = 0000000000000010
 3 = 0000000000000011
 4 = 0000000000000100
 5 = 0000000000000101
 6 = 0000000000000110
 7 = 0000000000000111
 8 = 0000000000001000
 9 = 0000000000001001
10 = 0000000000001010
11 = 0000000000001011
12 = 0000000000001100
"""

print("===========================")

# PRIORITAS OPERATOR

# Prioritas operator menggambarkan urutan pelaksanaan operasi.

# Tanda kurung memiliki prioritas tertinggi, yang berarti bahwa ekspresi di dalam tanda kurung harus dievaluasi terlebih dahulu :

print((6 + 3) - (6 + 3))

"""
Parenthesis have the highest precedence, and need to be evaluated first.
The calculation above reads 9 - 9 = 0
"""

print("===========================")

# Perkalian * mempunyai prioritas lebih tinggi daripada penjumlahan +, dan karenanya perkalian dievaluasi sebelum penjumlahan :

print(100 + 5 * 3)

"""
Multiplication has higher precedence than addition, and needs to be evaluated first.
The calculation above reads 100 + 15 = 115
"""
