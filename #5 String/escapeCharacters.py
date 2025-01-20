# ESCAPE KARAKTER

# Untuk menyisipkan karakter yang ilegal dalam suatu string, gunakan karakter escape. Karakter escape adalah garis miring terbalik \ diikuti oleh karakter yang ingin anda masukkan :

# Karakter escape memungkinkan anda menggunakan tanda kutip ganda ketika biasanya tidak diperbolehkan :

txt = "We are the so-called \"Viking\" from \f the north"
print(txt)

print("===========================")

# SINGLE QUOTES

txt = "We are the so-called \'Viking\' from 'the' north"
print(txt)

print("===========================")

# BACKSLASH

txt = "We are the so-called \\Viking\\ from the north"
print(txt)

print("===========================")

# NEW LINE

txt = "We are the so-called \nViking from the north"
print(txt)

print("===========================")

# CARRIAGE RETURN

txt = "Hello\rWorld!"
print(txt)

print("===========================")

# TAB

txt = "We are the so-called \tViking\t from the north"
print(txt)

print("===========================")

# BACKSPACE

txt = "We are the so-called \bViking\b from the north"
print(txt)

print("===========================")

# FORM FEED

txt = "We are the so-called \fViking from the north"
print(txt)

print("===========================")

# OCTAL VALUE

txt = "\110\145\154\154\157"
print(txt) 
print("===========================")

# HEX VALUE

txt = "\x48\x65\x6c\x6c\x6f"
print(txt) 