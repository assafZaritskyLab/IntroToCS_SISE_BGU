import copy


class Vector:
    """
    A class used to represent a vector.
    :attribute values: a list of numbers that describe the vector.
    """

    def __init__(self, lst):
        """
        Constructor for vector class.
        :param lst: a list of numbers
        """

        if not isinstance(lst, list):
            raise ValueError("Wrong parameter type")
        self.values = copy.copy(lst)
        # self.values = lst

    def __repr__(self):
        """
        print function override
        """
        return str(self.values)

    def __add__(self, vec):
        """
        addition operator overload
        :param vec: a Vector to be added to self
        """
        if (not isinstance(vec, Vector)) or (len(vec) != len(self)):
            raise ValueError("Wrong type or dimensions")
        res_lst = []
        for i in range(len(self)):
            res_lst.append(self[i] + vec[i])
        return Vector(res_lst)

    def __mul__(self, other):
        """
        multiplication operator overload
        :param other: a Vector or number to multiply with self
        """
        if isinstance(other, (int, float)):
            return Vector([other * x for x in self])
        if isinstance(other, Vector) and len(self) == len(other):
            return sum([self[i] * other[i] for i in range(len(self))])
        raise ValueError("Wrong type or dimensions")

    def __getitem__(self, i):
        """
        indexing operator overload
        :param i: index
        """
        return self.values[i]

    def __eq__(self, other):
        """
        == operator overload
        :param other: a Vector to check equality with self
        """
        if not isinstance(other, Vector):
            return False
        return self.values == other.values

    def __len__(self):
        """
        len function override
        """
        return len(self.values)

vec1 = Vector([3, 3, 7])
print(vec1 * 2.5)
print(2.5 * vec1)
