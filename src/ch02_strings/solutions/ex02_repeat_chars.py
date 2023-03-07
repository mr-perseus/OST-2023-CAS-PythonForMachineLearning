def repeat_chars(input):
    result = ""

    for i, ch in enumerate(input):
        result += ch * (i + 1)

    return result


print(repeat_chars("ABCD"))
print(repeat_chars("ABCDEF"))