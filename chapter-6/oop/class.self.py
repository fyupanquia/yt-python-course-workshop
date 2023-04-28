class Square:
    side = 8
    def area(self): # seld is a reference to an instance
        return self.side ** 2

sq = Square()
print(sq.area())  # side is found on the class
print(Square.area(sq)) # equivalent to sq.area()

sq.side = 10
print(sq.area()) # side is found on the instance