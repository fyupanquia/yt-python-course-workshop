class Weird:
    def __init__(self, s):
        self.s = s
    
    def __len__(self):
        return len(self.s)
    
    def __bool__(self):
        return '42' in self.s
    
weird = Weird('Hello! I am 9 years old!')
print(len(weird))
print(bool(weird))

weird2 = Weird('Hello! I am 42 years old!')
print(len(weird2))
print(bool(weird2))