class Counter:
    def __init__(self, count):
        self.__count = count

    def __str__(self):
        return f"Count = {self.__count}"

    def count(self):
        self.__count += 1

    def reset(self):
        self.__count = 0


def main():
    # Counter erzeugen, 2x hochzählen und dann resetten
    cnt = Counter(2)
    print(cnt)
    cnt.count()
    print(cnt)
    cnt.count()
    print(cnt)
    cnt.reset()
    print(cnt)


if __name__ == "__main__":
    main()