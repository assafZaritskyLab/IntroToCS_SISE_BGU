class square_all_it:
    def __init__(self, numbers):
        self.numbers = iter(numbers)

    def __next__(self):
        return next(self.numbers) ** 2

    def __iter__(self):
        return self


my_numbers = [x for x in range(10)]
squares_iterator = square_all_it(my_numbers)

print(squares_iterator)
print(next(squares_iterator))
print(next(squares_iterator))
print(next(squares_iterator))
print(next(squares_iterator))


