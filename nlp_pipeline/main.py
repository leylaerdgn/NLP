import string
from nltk.stem import PorterStemmer

# stemmer nesnesi
stemmer = PorterStemmer()


def clean_text(text):
    text = text.lower()

    text = ''.join(
        char for char in text
        if char not in string.punctuation
    )

    return text


def tokenize(text):
    return text.split()


def remove_stopwords(tokens):
    stopwords = [
        "ile",
        "çok",
        "bir",
        "ve",
        "ama",
        "bu"
    ]

    filtered_tokens = [
        word for word in tokens
        if word not in stopwords
    ]

    return filtered_tokens


def apply_stemming(tokens):
    stemmed_tokens = [
        stemmer.stem(word)
        for word in tokens
    ]

    return stemmed_tokens


def preprocess(text):

    # 1 cleaning
    text = clean_text(text)

    # 2 tokenize
    tokens = tokenize(text)

    # 3 stopwords
    tokens = remove_stopwords(tokens)

    # 4 stemming
    tokens = apply_stemming(tokens)

    return tokens


if __name__ == "__main__":

    text = "Python ile NLP öğreniyorum ve çok güzel projeler geliştiriyorum!!!"

    result = preprocess(text)

    print("Pipeline sonucu:")
    print(result)