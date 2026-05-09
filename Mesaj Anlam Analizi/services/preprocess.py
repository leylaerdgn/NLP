import string
from nltk.corpus import stopwords
from snowballstemmer import TurkishStemmer

stemmer = TurkishStemmer()

def metin_temizle(metin):
    temiz_metin =""
    for karakter in metin:
        if karakter not in string.punctuation:
            temiz_metin+=karakter
    return temiz_metin

def kucuk_harf_yap(metin):
    return metin.lower()

def stopwords_temizle(metin):
    stop_words = stopwords.words("turkish")
    kelimeler = metin.split()
    temiz_kelimeler= []
    for kelime in kelimeler:
        if kelime not in stop_words:
            temiz_kelimeler.append(kelime)
    return " ".join(temiz_kelimeler)

def kok_bul(metin):
    kelimeler=metin.split()

    kokler=[]
    for kelime in kelimeler:
        kok= stemmer.stemWord(kelime)
        kokler.append(kok)
    return " ".join(kokler)

def on_isleme(metin):
    metin = metin_temizle(metin)
    metin = kucuk_harf_yap(metin)
    metin = stopwords_temizle(metin)
    metin = kok_bul(metin)
    return metin