
def detect_code(text):
    keywords = ["def ", "import ", "print(", "for ", "while ", "class "]

    for word in keywords:
        if word in text:
            return True
    return False
