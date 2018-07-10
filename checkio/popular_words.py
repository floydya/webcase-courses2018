def popular_words(text, words):
    dct = {}
    text = text.lower()
    for i in words:
        dct[i] = text.count(i)
    return dct
