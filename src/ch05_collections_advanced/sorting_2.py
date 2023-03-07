names = ["tim", "TOM", "MIKE", "Michael", "andreas", "STEFAN"]
names.sort(key=str.lower)
print("lower", names)
names.sort(key=str.casefold)
print("casefold", names)


values = ["a", "cc", "bbb", "dddd", "ee", "f", "d", "eee"]
new_list = sorted(values, key=lambda x: (len(x), x))
print("sorted len + alpha values", new_list)

values = ["a", "cc", "bbb", "dddd", "ee", "f", "d", "eee"]
print(sorted(values, key=lambda x: (-len(x), x)))
values = ["a", "cc", "bbb", "dddd", "ee", "f", "d", "eee"]
print(sorted(values, key=lambda x: (len(x), x), reverse=True))


programmers = [("Tim", ["Java"]), ("Tom", ["Java", "Python"]),
               ("Michael", ["Java", "Python"]), ("Jim", ["Python"]),
               ("Polyglotti", ["Java", "Python", "C#", "C++"])]

print("ssorted programmers", sorted(programmers, key=lambda x: (-len(x[1]), x[0])))
