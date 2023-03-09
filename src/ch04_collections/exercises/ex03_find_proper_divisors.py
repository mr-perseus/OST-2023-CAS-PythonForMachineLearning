def find_proper_divisors(value):
    divisors = []
    for i in range(1, value // 2 + 1):
        if value % i == 0:
            divisors.append(i)
    return divisors


def find_proper_divisors_easy(value):
    return [x for x in range(1, value // 2 + 1) if value % x == 0]


print(find_proper_divisors(12))
print(find_proper_divisors_easy(12))
