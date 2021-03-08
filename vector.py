class Vector:

    def __init__(self, *args):
        self._coords = list(args)

    def __str__(self):
        return str(tuple(self._coords))

    def __len__(self):
        return len(self._coords)

    def __getitem__(self, k):
        return self._coords[k]

    def __setitem__(self, k, val):
        self._coords[k] = val

v = Vector(1, 2, 3)
v[-1] = 9

for c in v:
    print(c, end = " ")
print()
