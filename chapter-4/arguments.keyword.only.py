def func(*a, c):
    print(a, c)

func(1, 2, 3, c=7)
func(c=4)

def func2(a, b=2, *, c):
    print(a, b, c)

func2(3, b=5, c=99)
func2(3, c=13)