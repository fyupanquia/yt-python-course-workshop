squares = []
for n in range(10):
    squares.append(n ** 2)

print(squares)

squares = list(map(lambda n:n**2, range(10)))

print(squares)

squares = [n ** 2 for n in range(10)]

print(squares)