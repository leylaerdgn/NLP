import string
from nltk.corpus import stopwords

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
    kelimeler = metin.split
    temiz_kelimeler= []
    for kelime in kelimeler:
        if kelime not in stop_words:
            temiz_kelimeler.append(kelime)
    return " ".join(temiz_kelimeler)