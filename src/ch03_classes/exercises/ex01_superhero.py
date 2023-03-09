class SuperHero:
    def __init__(self, name, superpower, strength):
        self.name = name
        self.superpower = superpower
        self.__strength = strength

    def __str__(self):
        return f"Name: {self.name}; Superpower: ${self.superpower}; strength: {self.__strength}"

    def is_stronger_than(self, other):
        return self.__strength > other.__strength

    def strongest_of(*heros):
        strongest_hero = None
        for hero in heros:
            # if not isinstance(strongest_hero, SuperHero) or hero.__strength > strongest_hero.__strength:
            if strongest_hero is None or hero.__strength > strongest_hero.__strength:
                strongest_hero = hero

        return strongest_hero


def main():
    superman = SuperHero("Superman", "Kryptonite-Power", 1_000)
    batman = SuperHero("Batman", "Techno-Power", 100)
    ironman = SuperHero("Ironman", "Techno-Power", 500)

    print("Superman stronger than Batman?",
          superman.is_stronger_than(batman))
    print(SuperHero.strongest_of(superman, batman, ironman))


if __name__ == "__main__":
    main()