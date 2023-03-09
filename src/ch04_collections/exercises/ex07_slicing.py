values = [3, 4, 5, 8, 9]
print(values)

values.insert(0, 7)
values.insert(3, 42)
values.append(1337)
print(values)


values[4:7] = []
print(values)
values[1:-1] = []
print(values)
