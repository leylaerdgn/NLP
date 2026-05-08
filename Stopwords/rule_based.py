def remove_stopwords(tokens):
    stopwords = ["ve", "ile", "bir", "çok", "ama"]

    filtered_tokens = [
        word for word in tokens
        if word not in stopwords
    ]

    return filtered_tokens


tokens = [
    "ben",
    "bugün",
    "nlp",
    "ile",
    "çok",
    "güzel",
    "şeyler",
    "öğrendim"
]

sonuc = remove_stopwords(tokens)

print("Temizlenmiş:", sonuc)