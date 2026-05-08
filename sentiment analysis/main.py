from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Eğitim verisi
yorumlar = [
    "bu film çok güzeldi",
    "harika bir telefon",
    "çok memnun kaldım",
    "rezalet bir ürün",
    "hiç beğenmedim",
    "çok kötüydü"
]

etiketler = [
    "olumlu",
    "olumlu",
    "olumlu",
    "olumsuz",
    "olumsuz",
    "olumsuz"
]

# Metni sayıya çevir
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(yorumlar)

# Model oluştur
model = MultinomialNB()

# Eğit
model.fit(X, etiketler)

# Yeni yorum
yeni_yorum = ["telefon harika"]

# Sayıya çevir
yeni_vector = vectorizer.transform(yeni_yorum)

# Tahmin
tahmin = model.predict(yeni_vector)

print(tahmin[0])