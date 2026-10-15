 
import math


class Vector:
    def __init__(self, *components):
        self.components = components

    def __str__(self):
        return f"Vector({', '.join(map(str, self.components))})"

    def __repr__(self):
        return str(self)

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimension")

        result = [
            a + b
            for a, b in zip(self.components, other.components)
        ]

        return Vector(*result)

    def __sub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimension")

        result = [
            a - b
            for a, b in zip(self.components, other.components)
        ]

        return Vector(*result)

    def __mul__(self, other):
        if isinstance(other, Vector):
            if len(self.components) != len(other.components):
                raise ValueError("Vectors must have the same dimension")

            return sum(
                a * b
                for a, b in zip(self.components, other.components)
            )

        if isinstance(other, (int, float)):
            return Vector(*(a * other for a in self.components))

        return NotImplemented

    def __rmul__(self, other):
        return self * other

    def magnitude(self):
        return math.sqrt(
            sum(a ** 2 for a in self.components)
        )

    def normalize(self):
        length = self.magnitude()

        if length == 0:
            raise ValueError("Zero vector cannot be normalized")

        return Vector(*(a / length for a in self.components))


v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

print(v1)

v3 = v1 + v2
print(v3)
v4 = v2 - v1
print(v4)

dot_product = v1 * v2
print(dot_product)

v5 = 3 * v1
print(v5)

print(v1.magnitude())

v_unit = v1.normalize()
print(v_unit)

