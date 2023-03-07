from enum import Enum


class Direction(Enum):
     N = (0, -1)
     NE = (1, -1)
     E = (1, 0)
     SE = (1, 1)
     S = (0, 1)
     SW = (-1, 1)
     W = (-1, 0)
     NW = (-1, -1)


print(Direction.NE.value)
ne = Direction.NE
print(ne.value[0], "/", ne.value[1])