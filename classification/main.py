import pandas as pd #pandas, CSV gibi tablo dosyalarını okumamızı sağlar.

from sklearn.feature_extraction.text import CountVectorizer #Bu satır, metni sayıya çevirmek için kullanılır.
from sklearn.naive_bayes import MultinomialNB #MultinomialNB, metin sınıflandırmada sık kullanılan basit bir modeldir.

# CSV dosyasını oku
df = pd.read_csv("spam.csv")

# Mesajlar
X = df["mesaj"]

# Etiketler
y = df["etiket"]

# Metinleri sayıya çevir
vectorizer = CountVectorizer()

X_vector = vectorizer.fit_transform(X)

# Model oluştur
model = MultinomialNB()

# Modeli eğit
model.fit(X_vector, y)

# Yeni mesaj
yeni_mesaj = ["bedava telefon kazandınız"]

# Yeni mesajı sayıya çevir
yeni_vector = vectorizer.transform(yeni_mesaj)

# Tahmin yap
tahmin = model.predict(yeni_vector)

print("Tahmin:", tahmin[0])