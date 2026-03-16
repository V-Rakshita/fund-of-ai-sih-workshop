bad_words = [
    "stupid",
    "idiot",
    "dumb",
    "hell",
    "shit"
]

def check_bad_language(text):
    for word in bad_words:
        if word in text.lower():
            return True
    return False