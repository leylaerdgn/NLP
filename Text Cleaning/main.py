import string #Pythonun hazır string modülünü çağırıyoruz. Bu modülün içinde hazır noktalama işaretleri var. Biz bunu noktalama işaretlerini silmek için kullanacağız.

def clean_text(text):
    #1 lowercase
    text=text.lower()

    #2 noktalama
    text= ''.join(char for char in text if char not in string.punctuation)
    
    #3 tokenize
    tokens=text.split()

    #4 stopword
    stopwords= ["ile" , "çok", "bir"]
    tokens= [word for word in tokens if word not in stopwords]
    
    return tokens


text = "Bugün Python ile NLP çalıştım!!! Çok güzel bir gündü :)"
print(clean_text(text))