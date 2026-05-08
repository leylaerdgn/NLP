## Tokenization
    Bir metni küçük parçalara (token) ayırma işlemidir.
    bu parçalar genellikle kelime,cümle, karakter olabilir.

## Token
    Parçalanmış en küçük anlamlı birimdir.
    "Bugün NLP öğreniyorum" -> ["Bugün", "NLP", "öğreniyorum"]

## TOKENİZATİON TÜRLERİ

# 1. Word Tokenization
Kelime bazlı tokenlara ayırır.

# 2. Sentence Tokenization
Cümle bazlı tokenlara ayırır.

# 3. Character Tokenization
Karakter bazlı tokenlara ayırır.

Burası öenlidir çünkü NLP kelimelerle çalışır metin direkt işlenmez. Tokenize etmeden önce temizleme işlemi yapılır çünkü split yetmez!

## BAZI KOD SATIRLARI VE ANLAMI (regex_based)
    Regex (Regular Expressions - Düzenli İfadeler), metinler içinde belirli karakter dizilerini veya kalıpları (desenleri) aramak, eşleştirmek, bulmak ve değiştirmek için kullanılan özel bir söz dizimi yapısıdır

    findall(): metin içinde verdiğin kurala uyan HER şeyi bulur ve liste olarak döndürür. iki parametre alır: re.findall(pattern, text)
    | Parametre | Anlam                        |
    | --------- | ---------------------------- |
    | `pattern` | NEYİ arayacağını söylersin   |
    | `text`    | NEREDE arayacağını söylersin |
    
    birinci parametre aslında küçük bir regex dili : 
    \d: sayı demek (0-9)
    +: bir veya daha fazla
    \d+ = sayıları bul
    r = "bunu aynen al"
    \w = harf
    r'\w+' = kelime bul
    \s = boşluk

---------------------------------------------------

## 1. Metin Temizleme
    Ham metni, anlamlı ve işlenebilir hale getirme sürecidir. Amaç: gereksiz karakterleri silmke, metni standart hale getirmek, modelin daha doğru öğrenmesini sağlamaktır.

## 2. Lowercase (küçül harfe çevirme)
    tüm harfleri küçük harf yapar çünkü: 
    "NLP" ≠ "nlp"
    o yüzden kelimeler tek formata indirgenir.

## 3. Noktalama Temizleme
    Virgül, nokta, ünlem gibi işaretler kaldırılır. Çünkü anlam taşımazlar ve modeli yanıltabilirler.
    Örnek: "merhaba!!!" → "merhaba"
    string.punctuation: Noktalama karakterlerinin hazır listesi.

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

---------------------------------------------------

## Stopwords
Metinde çok sık geçen ama genelde anlam taşımayan kelimelerdir. Bu kelimeler genellikle silinir.

------------------------------------------------

## Stemming and Lemmatization
Burası kelimenin kökünü bulur

Stemming: kural tabanlı şekilde budama
örnek: playing -> play
       running -> run
Stemming algoritmaları var:
Örneğin:
Porter Stemmer
Snowball Stemmer

- >Porter Stemmer
Kelimenin kökünü bulmak için yazılmış hazır sistemdir. 



👉 bunlar yıllardır geliştirilmiş algoritmalar.
Lemmatization: Gerçek sözlük formuna dönüştürme
örnek: running -> run
       better -> good


-------------------------------------------------

## Vektörleştirme
Bilgisayar metni doğrudan anlayamaz. Modelin bunu anlayabilmesi için metni sayıya çevirmemiz gerekir.

- >Bag of Words
Metinde hangi kelimenin kaç kez geçtiğine bakar.
Örnek: 
    texts = [
        "python öğreniyorum",
        "nlp öğreniyorum",
        "python nlp güzel"
    ]
Kelime havuzu:
güzel, nlp, python, öğreniyorum

Sonra her cümle sayıya çevrilir:
"python öğreniyorum" → [0, 0, 1, 1]
"nlp öğreniyorum"    → [0, 1, 0, 1]
"python nlp güzel"   → [1, 1, 1, 0]

- >bag_of_words.py
feature_extraction.text: metinden özellik çıkarma kısmı
CountVectorizer: kelime sayılarını vektöre çeviren araç
X = vectorizer.fit_transform(texts): 
fit(): kelimeleri öğrenir
transform(): metni sayıya çevirir

print(vectorizer.get_feature_names_out()): Bu satır, CountVectorizer’ın metinlerden öğrendiği kelime listesini gösterir.

X.toarray(): X, fit_transform() sonucunda oluşan sayısal veridir. Ama X normalde ekrana direkt okunabilir tablo gibi basılmaz. Çünkü scikit-learn bunu genellikle sparse matrix denen daha verimli bir yapıda tutar.

- >TF-IDF
Bag of Words sadece sayar.Ama TF-IDF daha akıllıdır.
"bir", "ve", "çok"
çok geçebilir ama çok anlamlı olmayabilir.

TF-IDF şuna bakar:
Bu kelime bu metin için ne kadar önemli?
Yani sık geçen ama her metinde olan kelimelerin önemini azaltır.
| Değer      | Anlam       |
| ---------- | ----------- |
| 0          | kelime yok  |
| küçük sayı | az önemli   |
| büyük sayı | daha önemli |

-------------------------------------------------

## Classification
Bu kısım NLP’de artık “metni temizledim, parçaladım, vektöre çevirdim” aşamasından sonra gelen model kurma mantığıdır.
Classification = sınıflandırma demek. Yani modele bir metin veriyoruz, model de bu metnin hangi sınıfa ait olduğunu tahmin ediyor.
Örnek:
"Bu ürün çok güzel" → olumlu
"Hiç beğenmedim" → olumsuz

veya:

"Bedava kazandınız, hemen tıklayın" → spam
"Toplantı yarın saat 10'da" → spam değil

- >example.py dosyası
df = pd.read_csv("spam.csv")
df dediğimiz şey artık Python’daki tablo gibidir.
Örneğin:
mesaj	                    etiket
ücretsiz kazandınız	         spam
toplantı yarın saat 3te	     normal

X = df["mesaj"]
Burada mesaj sütununu alıyoruz.
Yani modelin bakacağı metinler:
ücretsiz kazandınız
hemen tıklayın
toplantı yarın saat 3te

y = df["etiket"]
Burada da cevapları alıyoruz.
Yani her mesajın doğru etiketi:
spam
spam
normal

-------------------------------------------

## Sentiment Analysis (Duygu Analizi)
Bir metnin duygusunu anlamaya çalışmak.

Genelde sınıflar şunlar olur:
olumlu (positive)
olumsuz (negative)
bazen nötr (neutral)

-Sentiment analysis özel bir classification türüdür.

Model şunu öğrenir:
güzel → olumluya yakın
harika → olumluya yakın
rezalet → olumsuza yakın

- >main.py
- >from sklearn.naive_bayes import MultinomialNB:
Naive Bayes adlı sınıflandırma modelini kullan.
Naive Bayes, olasılık mantığıyla çalışan bir sınıflandırma algoritmasıdır. Amacı bir verinin hangi sınıfa ait oldugunu tahmin etmek. 
Örneğin:
spam / normal
olumlu / olumsuz
MultinomialNB: MultinomialNB, Naive Bayes’in metin verileri için kullanılan versiyonudur. Özellikle kelime sayıları, kelime frekansları ile çalışır.

- >X = vectorizer.fit_transform(yorumlar)
fit → kelimeleri öğren
transform → metni sayıya çevir
Buradaki X, yorumların sayıya çevrilmiş halidir.
yorumlar → metin hali
X → sayısal hali

- >model.fit(X, etiketler)
Bu satırda model öğrenir. 
Sayılar	   Doğru cevap
[1,0,1,0]	olumlu
[0,1,0,1]	olumsuz
ve öğrenmeye çalışıyor:
Hangi sayı düzeni hangi etikete ait?
Diyoruz ki:
Bu sayı düzeni → olumlu
Bu sayı düzeni → olumsuz
Model örneklerden desen öğreniyor.