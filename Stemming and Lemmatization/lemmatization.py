from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

words = ["running", "better", "studies"]

for word in words:
    print(word, "→", lemmatizer.lemmatize(word, pos='v')) #pos='v': verb