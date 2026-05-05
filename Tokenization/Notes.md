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
