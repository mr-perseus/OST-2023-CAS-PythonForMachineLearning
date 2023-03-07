import random

sample_names = ["TIM", "TOM", "MIKE", "JOHN", "MICHAEL", "STEFAN"]


def choose_greeting():
    return random.choice(["MOIN", "GRÜEZI", "HALLO", "TACH"])


greet_double_named = list(map(lambda str: choose_greeting() + " " + (str + " ") * 2, sample_names))
print(greet_double_named)

