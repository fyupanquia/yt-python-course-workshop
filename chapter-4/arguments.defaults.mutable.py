def func(a=None, b={}):
    if(a is None):
        a=[]
    
    print(a)
    print(b)
    print('#'*12)
    a.append(len(a))
    b[len(a)] = len(a)

func()
func()
func()