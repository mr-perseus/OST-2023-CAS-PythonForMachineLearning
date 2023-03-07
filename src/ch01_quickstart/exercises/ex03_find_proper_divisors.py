def find_proper_divisors(value):
    divisors = []
    current_factor = 2
    value_remaining = value

    while value_remaining != 1:
        if (value_remaining % current_factor) == 0:
            divisors.append(current_factor)
            value_remaining = value_remaining / current_factor
        else:
            current_factor += 1

    return divisors


print(find_proper_divisors(12))
print(find_proper_divisors(22))
print(find_proper_divisors(6))
print(find_proper_divisors(1337))
print(find_proper_divisors(1024))
