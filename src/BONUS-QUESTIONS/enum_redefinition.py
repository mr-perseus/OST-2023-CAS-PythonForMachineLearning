from enum import Enum, auto


class Size(Enum):
    XS = auto()
    S = auto()
    M = auto()
    L = auto()
    XL = auto()
    XXL = auto()


shirt_size = Size.XL
print(shirt_size)

# redefinition => AttributeError: Cannot reassign members.
Size.XXL = 47
print(Size.XXL)
