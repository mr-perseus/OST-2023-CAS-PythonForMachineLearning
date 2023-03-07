def remove_vowel(text):
    result = ""

    for letter in text:
        if letter not in "AÄEIOÖUüaäeioöuü":
            result += letter

    return result


def replace_vowel(text):
    result = ""

    for letter in text:
        if is_vowel(letter):
            result += '_'
        else:
            result += letter

    return result


def is_vowel(letter):
    return letter in "AÄEIOÖUüaäeioöuü"


print(remove_vowel("Es gibt viel zu entdecken!"))

print(replace_vowel("Es gibt viel zu entdecken!"))

text = "PYTHON INTRO BY MICHAEL"
print(replace_vowel(text))