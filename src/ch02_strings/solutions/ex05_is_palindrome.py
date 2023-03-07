def is_palindrome(input):
    left = 0
    right = len(input) - 1
    lower_input = input.lower()
    is_same_char = True
    while left < right and is_same_char:
        is_same_char = (lower_input[left] == lower_input[right])
        left += 1
        right -= 1
    return is_same_char


print(is_palindrome("AbBa"))
print(is_palindrome("Michael"))
print(is_palindrome("was it a car or a cat i saw".replace(" ", "")))