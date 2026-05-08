from sklearn.feature_extraction.text import TfidfVectorizer

texts = [
    "python öğreniyorum",
    "nlp öğreniyorum",
    "python nlp güzel"
]

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(texts)

print("Kelimeler:")
print(vectorizer.get_feature_names_out())

print("\nTF-IDF Vektörleri:")
print(X.toarray())