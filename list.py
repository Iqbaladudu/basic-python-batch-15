foods = []

# Menambahkan data baru di ujung
foods.append("Seblak")
foods.append("Rendang")
foods.append("Ayam Bakar")

# Menghapus nilai ke x
foods.pop(1)

# Mendapatkan panjang dari list
print(len(foods))

for food in foods:
    print(food)