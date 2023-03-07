def find_proper_divisors(value):
    divisors = []
    for i in range(1, value // 2 + 1):
        if value % i == 0:
            divisors.append(i)
    return divisors


print(find_proper_divisors(12))


# Variante mit Vorbelegung und Listen-Addition
def find_proper_divisors_v2(value):
    divisors = [1]
    for i in range(2, value // 2 + 1):
        if value % i == 0:
            divisors += [i]
    return divisors


print(find_proper_divisors_v2(12))


def main():
    print(find_proper_divisors(12))
    print(find_proper_divisors_v2(12))


if __name__ == "__main__":
    main()