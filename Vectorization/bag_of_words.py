from sklearn.feature_extraction.text import CountVectorizer

texts = [
    "python öğreniyorum",
    "nlp öğreniyorum",
    "python nlp güzel"
]

vectorizer = CountVectorizer()

X = vectorizer.fit_transform(texts)

print("Kelimeler:")
print(vectorizer.get_feature_names_out())

print("\nVektörler:")
print(X.toarray())