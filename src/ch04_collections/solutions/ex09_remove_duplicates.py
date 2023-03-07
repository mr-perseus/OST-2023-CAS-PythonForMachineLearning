def remove_duplicates(inputs):
    result = []
    already_found_numbers = set()
    for i, elem in enumerate(inputs):
        if elem not in already_found_numbers:
            already_found_numbers.add(elem)
            result.append(elem)
    return result


print(remove_duplicates([7, 2, 7, 1]))
print(remove_duplicates([1, 6, 6, 6, 1, 2]))
