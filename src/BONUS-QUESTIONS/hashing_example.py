class Dog():
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def __str__(self):
        return f"Name: {self.name} / Rasse: {self.breed}"

    def __repr__(self):
        return self.__str__()

    #########################################

    def __eq__(self, other):
        if not isinstance(other, Dog):
            return False

        return self.name == other.name and \
               self.breed == other.breed

    def __hash__(self):
        # hash(custom_object)
        return hash((self.name, self.breed))


    # QUESTION: static methods
    def trick_add_numbers(x, y):
        return x + y

    #########################################

dog1 = Dog("Rex", "German")
dog2 = Dog("Rex", "German")
dog3 = Dog("Sarah", "Collie")
dog4 = Dog("King", "Dobermann")

dogs = {dog1, dog2, dog3, dog4}

for dog in dogs:
    print(dog)

print(Dog.trick_add_numbers(7, 12))