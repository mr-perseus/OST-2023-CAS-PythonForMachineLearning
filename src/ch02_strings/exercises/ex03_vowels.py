import re


def remove_vowel(text):
    return re.sub("[aeiouAEIOU]", "", text)


def replace_vowel(text):
    return re.sub("[aeiouAEIOU]", "_", text)


text = "Es gibt viel zu entdecken!"
print(remove_vowel(text))

text = "Es gibt viel zu entdecken!"
print(replace_vowel(text))

text = "PYTHON INTRO BY MICHAEL"
print(replace_vowel(text))