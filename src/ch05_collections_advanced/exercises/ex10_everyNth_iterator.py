class EveryNth:
    def __init__(self, values, step, pos=0):
        self.values = values
        self.step = step
        self.pos = pos

    def __iter__(self):
        return self

    def __next__(self):
        if self.pos >= len(self.values):
            raise StopIteration

        result = self.values[self.pos]
        self.pos += self.step
        return result


thirdst_list = EveryNth([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 3)
print(list(thirdst_list))

thirdst_list = EveryNth([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 4, 2)
print(list(thirdst_list))

fifth_list = EveryNth([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 5)
print(list(fifth_list))
