from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

words = ["playing", "running", "studies"]

for word in words:
    print(word, "→", stemmer.stem(word))