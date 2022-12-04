import math
import os

os.system ("clear")
print(f"{'PENGGUNAAN lambda':^30}")
print("="*30)

# def a(x):
#     return x**2

a = lambda x : x**2

nilai_x = int(input("Masukkan nilai x : "))
hasil = a(nilai_x)
print(hasil)

print("="*30)

# def b(x, y):
#     return math.sqrt(x**2 + y**2)

b = lambda x, y : math.sqrt(x**2 + y**2)

nilai_x = int(input("Masukkan nilai x : "))
nilai_y = int(input("Masukkan nilai y : "))
hasil=b(nilai_x, nilai_y)
print(f"{hasil:2f}")

print("="*30)

# def c(*args):
#     return sum(args)/len(args)

c = lambda *args : sum(args)/len(args)
hasil = c(nilai_x, nilai_y)
print(hasil)

print("="*30)

# def d(s):
#     return "".join(set(s))

d = lambda s : "".join(set(s))
nama_s = input("Masukkan nama : ")
hasil = d(nama_s)
print(hasil)
