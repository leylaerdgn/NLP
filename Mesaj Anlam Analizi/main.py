from services.csv_reader import verileri_oku

df = verileri_oku()

X= df["mesaj"]
y= df["etiket"]

print("Mesajlar: ")
print(X)

print("\nEtiketler:")
print(y)

