word = 'Hello'
swaps = {c: c.swapcase() for c in word}
print(swaps)

positions = {c: k for k, c in enumerate(word)}
print(positions)