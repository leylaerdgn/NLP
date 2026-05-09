def tahmin_et(yeni_mesaj, model, vectorizer, on_isleme):
    temiz_mesaj=on_isleme(yeni_mesaj)
    mesaj_vector =vectorizer.transform([temiz_mesaj])
    tahmin =model.predict(mesaj_vector)
    return tahmin[0], temiz_mesaj