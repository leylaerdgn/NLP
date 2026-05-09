# Bu dosya model oluşturma, eğitme, döndürme gibi modelle ilgili işlemler yapacak.
from sklearn.naive_bayes import MultinomialNB
def modeli_egit(X_vector, y):
    model = MultinomialNB() #metin sınıflandırmada sık kullanılan basit bir model

    model.fit(X_vector,y) # → modele “bu vektör şu etikete ait” diye öğretir

    return model