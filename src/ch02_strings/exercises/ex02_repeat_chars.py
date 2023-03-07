import pytest


def repeat_chars(input):
    result = ""
    for index, character in enumerate(input):
        result += character * (index + 1)

    return result


print(repeat_chars("ABCD"))
print(repeat_chars("ABCDEF"))


@pytest.mark.parametrize("test_input,expected",
                         [("ABCD", "ABBCCCDDDD"), ("ABCDEF", "ABBCCCDDDDEEEEEFFFFFF")])
def test_eval(test_input, expected):
    assert repeat_chars(test_input) == expected