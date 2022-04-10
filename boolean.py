a = 34 > 33
print(a)
b = 0
print(f"angka NOL: {bool(b)}")

bilangan_pertama = int(input("Masukkan bilangan pertama: "))
bilangan_kedua = int(input("Masukkan bilangan kedua: "))

if bilangan_pertama > bilangan_kedua:
    print(f"Bilangan {bilangan_pertama} lebih besar dari {bilangan_kedua}")
elif bilangan_pertama < bilangan_kedua:
    print(f"bilangan {bilangan_pertama} lebih kecil dari {bilangan_kedua}")