def count_words(text, words):
    total = []
    text = text.lower()
    for w in words:
        if 3 <= len(w) and w.islower() and w.isalpha():
            if w in text:
                total.append(w)
    return len(list(set(total)))
