# 1. ADIM: CSV dosyası yazma.
ilk olarak csv dosyamı yazdım ve ilk satrı mesaj,etiket şeklinde çünkü python ilk satırı kolon adı alır.

# 2. ADIM:  Service katmanı
gerçek projelerde veri üzerinde işlem yapan kodlar genelde service katmanında olur!
burada csv_reader.py dosyasını açtık. Buradareturn df ile okunan csv verisini geri döndürdum. Yani başka dosyalar bu veriyi kullanabilsin diye
read_csv pandas kütüphanesinin bir fonksiyonudur.
çalıştırdıktan sonra bir dataframemimiz oldu