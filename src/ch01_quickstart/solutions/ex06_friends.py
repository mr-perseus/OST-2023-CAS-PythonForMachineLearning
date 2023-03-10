from src.ch01_quickstart.solutions.ex03_find_proper_divisors import find_proper_divisors


def calc_friends(max_exclusive):
    friends = {}
    for i in range(2, max_exclusive):
        divisors1 = find_proper_divisors(i)
        sum_div1 = sum(divisors1)
        divisors2 = find_proper_divisors(sum_div1)
        sum_div2 = sum(divisors2)

        if i == sum_div2 and sum_div1 != sum_div2:
            friends[i] = sum_div1

    return friends


print(calc_friends(1000))