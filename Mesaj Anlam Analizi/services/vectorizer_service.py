from sklearn.feature_extraction.text import CountVectorizer

def vektore_cevir(metinler):
    vectorizer=CountVectorizer()
    X_vector= vectorizer.fit_transform(metinler)
    return X_vector,vectorizer

