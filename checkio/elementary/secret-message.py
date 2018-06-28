def find_message(text):
    newtxt = ""
    for i in text:
        if i.isupper():
            newtxt += i
    return newtxt
