## Squere all generator
def square_all_gen(numbers):
    for n in numbers:
        yield n ** 2


my_numbers = [x for x in range(10)]
squere_all_gen = square_all_gen(my_numbers)
print(squere_all_gen)
print(next(squere_all_gen))
print(next(squere_all_gen))
print(next(squere_all_gen))
print(next(squere_all_gen))
