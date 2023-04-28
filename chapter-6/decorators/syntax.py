def func(arg1, arg2, ...):
    pass

func = dec1(dec2(func))
func = decoarg(arg_a, arg_b)(func)

#

@decorator1
@decorator2
def func(arg1, arg2, ...):
    pass

@decoarg(arg_a, arg_b)
def func(arg1, arg2, ...):
    pass
