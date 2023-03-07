import pytest


def is_palindrome(input):
    input_lower = input.lower()

    half_index = len(input_lower) // 2

    half_index_reversed = half_index if len(input) % 2 != 0 else half_index - 1

    return input_lower[0:half_index] == input_lower[:half_index_reversed:-1]


print(is_palindrome("AbBa"))
print(is_palindrome("Michael"))
print(is_palindrome("was it a car or a cat i saw".replace(" ", "")))


@pytest.mark.parametrize("test_input,expected",
                         [
                             ("AbBa", True),
                             ("ABCDEF", False),
                             ("a", True),
                             ("abccba", True),
                             ("abcdcba", True),
                             ("wasitacaroracatisaw", True),
                         ])
def test_eval(test_input, expected):
    assert is_palindrome(test_input) == expected
