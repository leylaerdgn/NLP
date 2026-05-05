## 1. Metin Temizleme
    Ham metni, anlamlı ve işlenebilir hale getirme sürecidir. Amaç: gereksiz karakterleri silmke, metni standart hale getirmek, modelin daha doğru öğrenmesini sağlamaktır.

## 2. Lowercase (küçül harfe çevirme)
    tüm harfleri küçük harf yapar çünkü: 
    "NLP" ≠ "nlp"
    o yüzden kelimeler tek formata indirgenir.

## 3. Noktalama Temizleme
    Virgül, nokta, ünlem gibi işaretler kaldırılır. Çünkü anlam taşımazlar ve modeli yanıltabilirler.
    Örnek: "merhaba!!!" → "merhaba"

## 4. Tokenization (Parçalama)
    Cümleyi kelimelere bölme işlemidir.
    örnek: "merhaba nlp öğreniyorum"
    ↓
    ["merhaba", "nlp", "öğreniyorum"]
    Amacımız metni analiz edilebilir parçalara ayırmaktır.

## 5. Stopwords (Gereksiz Kelimeler)
    Anlam taşımayan sık kullanılan kelimelerdir. Bunlar metinden analiz kısmında çıakrılır.
    örnek: "ve", "bir", "çok", "ama", "ile"
 
## 6. Stemming / Lemmatization
    Kelimeyi kök haline indirger. Amacımız Aynı anlamdaki kelimeleri birleştirmek.
    örnek:"çalışıyorum" → "çalış"
    "running" → "run"

GENEL AKIŞ:
Ham Metin
↓
Lowercase
↓
Noktalama Temizleme
↓
Tokenization
↓
Stopwords Removal
↓
Temiz Metin

## NLTK nedir?
NLTK (Natural Language Toolkit)
Python’da doğal dil işleme (NLP) yapmak için kullanılan bir kütüphanedir.
Kolaylıkları arasında;
-metinle çalışmayı kolaylaştırır.
-hazır araçlar sunar.

## MAİN.PY DOSYASINDAKİ BAZI SATIRLAR
- > import string
    String kütüphanesi bize harfler, sayılar, noktalama,boşluklar gibi kolaylıklar sağlar. biz punctuation kullandık, bu string kütüphanesindeki noktalama karakterlerinin listesini döndüren punctuation özelliğini kullandık.

- >    text= ''.join(char for char in text if char not in string.punctuation)
    Bu satırı 3 parçaya bölelim:
    1. for char in text: metindeki HER karakteri tek tek gez
    2. if char not in string.punctuation: eğer bu karakter noktalama değilse al
    3. ''.join(...): seçtiğin karakterleri tekrar birleştir
    örnek: 
        karakterler: m e r h a b a ! ! !   : )
        filtre: m e r h a b a (noktalamalar gitti)
        sonuç: "merhaba"

- >tokens = [word for word in tokens if word not in stopwords]
    Token listesindeki her kelimeye bak.
    Eğer kelime stopwords listesinde yoksa onu tut.
    Varsa çıkar.