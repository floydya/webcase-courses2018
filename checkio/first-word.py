import string
def first_word(text: str) -> str:
    if "..." in text:
        text = text.replace("...", "")
    for x in string.punctuation:
        if x != "'":
            text = text.replace(x," ")
    if text[0] == " ":
        text = text[1:]
    text = text.split(" ")
    return text[0]
