def compare_sums(side1, side2, side3):
    print(side1, side2, side3)
    return side1 == side2 and side2 == side3


def is_magic6(values):
    return compare_sums(sum(list(values[0:3])), sum(list(values[2:5])), sum(list(values[4:6] + [values[0]])))


print(is_magic6([1, 5, 3, 4, 2, 6]))
print(is_magic6([1, 2, 3, 4, 5, 6]))


def is_magic_triangle(values):
   pass


print(is_magic_triangle([1, 5, 3, 4, 2, 6]))
print(is_magic_triangle([1, 2, 3, 4, 5, 6]))
