cubes = [k**3 for k in range(10)]
print(cubes)
print(type(cubes))

cubes = (k**3 for k in range(10))
print(cubes)
print(type(cubes))
print(list(cubes))