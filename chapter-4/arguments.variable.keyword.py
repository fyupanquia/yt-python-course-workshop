def func(**kwargs):
    #print(kwargs)
    print(kwargs.get('a'))

func(a=1, b=2)
func(**{'a':1, 'b':2})
func(**dict(a=1, b=2))