def print_squares(start, end):
    #for n in range(start, end):
    #    yield n ** 2
    yield from (n ** 2 for n in range(start, end))


for n in print_squares(2, 5):
    print(n)