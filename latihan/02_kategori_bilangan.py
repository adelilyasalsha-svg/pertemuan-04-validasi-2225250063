bilangan = float(input("Masukkan bilangan: "))

if bilangan > 0:
    kategori = "Positif"
elif bilangan < 0:
    kategori = "Negatif"
else:
    kategori = "Nol"

print("Kategori:", kategori)