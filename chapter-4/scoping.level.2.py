def outer():
    test = 1 # this is defined in the local scope of the function
    def inner():
        test = 2 # inner scope
        print('inner: ', test)
    inner()
    print('outer:', test)

test = 0 # this is defined in the global scope
outer()
print('global: ', test)