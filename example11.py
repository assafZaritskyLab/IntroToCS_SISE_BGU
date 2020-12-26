my_numbers = [x for x in range(10)]
square_all_gen = (n ** 2 for n in my_numbers)
print(square_all_gen)
for x in square_all_gen:
    print(x)


