def remove_duplicates(inputs):
    new_inputs = []

    for entry in inputs:
        if entry not in new_inputs:
            new_inputs.append(entry)

    return new_inputs
    # return [x for x in inputs if x not in inputs[0:x]]
    # return [x for x in inputs if ]


print(remove_duplicates([7, 2, 7, 1]))
print(remove_duplicates([1, 6, 6, 6, 1, 2]))
