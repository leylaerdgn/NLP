# 1. ADIM: CSV dosyası yazma.
ilk olarak csv dosyamı yazdım ve ilk satrı mesaj,etiket şeklinde çünkü python ilk satırı kolon adı alır.

# 2. ADIM:  Service katmanı
gerçek projelerde veri üzerinde işlem yapan kodlar genelde service katmanında olur!
burada csv_reader.py dosyasını açtık. Buradareturn df ile okunan csv verisini geri döndürdum. Yani başka dosyalar bu veriyi kullanabilsin diye
read_csv pandas kütüphanesinin bir fonksiyonudur.
çalıştırdıktan sonra bir dataframemimiz oldu

# NOTLAR
- >corpus
içinde çok fazla yazı bulunan veri arşivi.NLP'DE NEDEN ÖNEMLİ?
Çünkü NLP sistemleri:
✔ dili öğrenmek
✔ analiz yapmak
✔ kelime istatistiği çıkarmak
için çok fazla metne ihtiyaç duyar.

| Corpus        | İçerik             |
| ------------- | ------------------ |
| stopwords     | gereksiz kelimeler |
| wordnet       | sözlük/veri tabanı |
| gutenberg     | kitaplar           |
| movie_reviews | film yorumları     |

- >snowballstemmer
bir stemming kütüphanesi.
- >TurkishStemmer
Türkçe kelimeleri köke indiren algoritma.
- >accuracy_score:
Model kaç tanesini doğru bildi?
- > classification_report
Her sınıf için precision, recall, f1-score gibi detaylı ölçümleri gösterir.  

------------------------------------------
X_train → modelin çalışacağı/eğitileceği mesajlar
y_train → bu mesajların doğru etiketleri

X_test → modelin hiç görmediği mesajlar
y_test → bu mesajların gerçek cevapları

--------------------------------
evulation_Service.py

- >accuracy = accuracy_score(y_test, y_pred)
burada şu karşılaştırılır:

y_test  → gerçek cevaplar
y_pred  → modelin tahmin ettiği cevaplar

Yani örnek olarak:

Gerçek: şikayet
Tahmin: şikayet
→ doğru

Gerçek: öneri
Tahmin: soru
→ yanlış

- >report = classification_report(y_test, y_pred)
classification_report ise daha detaylı tablo verir:

Precision: Model bir etiketi tahmin ettiğinde ne kadar doğru tahmin etmiş? (Model 5 mesaja “şikayet” dedi. Bunların 4 tanesi gerçekten şikayetse precision yüksektir.)

Recall: Gerçekten o etikete ait olan verilerin kaçını yakalayabildi? (Gerçekte 5 tane şikayet mesajı vardı. Model bunların 3 tanesini şikayet diye bulduysa recall 3/5 olur.)

F1-score: Precision ve recall değerlerinin dengeli ortalamasıdır.Yani model hem doğru tahmin ediyor mu hem de ilgili sınıfı iyi yakalıyor mu, bunu tek skorla gösterir.

Support: Test verisinde o etiketten kaç tane olduğunu gösterir. demek, test verisinde 2 tane gerçek şikayet mesajı var demektir.