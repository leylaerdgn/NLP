import string

def tokenize_manual(text):
    # lowercase
    text = text.lower()
    
    # noktalama temizleme
    text = ''.join(char for char in text if char not in string.punctuation)
    
    # tokenize
    tokens = text.split()
    
    return tokens


if __name__ == "__main__":
    text = "Merhaba!!! Bugün NLP öğreniyorum :) Çok güzel değil mi?"
    print("Rule Based:", tokenize_manual(text))