from services.csv_reader import verileri_oku
from services.preprocess import on_isleme
from services.vectorizer_service import vektore_cevir
from services.model_service import modeli_egit
from services.prediction_service import tahmin_et
from sklearn.model_selection import train_test_split
from services.evulation_service import modeli_degerlendir

df = verileri_oku()

X = df["mesaj"]
y = df["etiket"]

temiz_mesajlar = []

for mesaj in X:
    temiz_mesaj = on_isleme(mesaj)
    temiz_mesajlar.append(temiz_mesaj)

X_vector, vectorizer = vektore_cevir(temiz_mesajlar)

X_train, X_test, y_train, y_test = train_test_split(
    X_vector,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y #Bu, veriyi bölerken sınıf dağılımını korumaya çalışır.
)

model = modeli_egit(X_train, y_train)

accuracy, report = modeli_degerlendir(model, X_test, y_test)

print("Temizlenmiş Mesajlar:")
print(temiz_mesajlar)

print("\nKelimeler:")
print(vectorizer.get_feature_names_out())

print("\nVektörler:")
print(X_vector.toarray())

print("\nEtiketler:")
print(y)

print("\n--- Yeni Mesaj Tahmini ---")

yeni_mesaj = input("Bir müşteri mesajı girin: ")

tahmin, temiz_mesaj = tahmin_et(
    yeni_mesaj,
    model,
    vectorizer,
    on_isleme
)

print("Temizlenmiş yeni mesaj:", temiz_mesaj)
print("Tahmin edilen etiket:", tahmin)