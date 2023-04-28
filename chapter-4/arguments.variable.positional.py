def minimum(*n):
    print(type(n))
    if n:
        mn= n[0]
        for value in n[1:]:
            if value < mn:
                mn = value
        print(mn)

values = (1, 3, -7, 9)
minimum(*values) # minimum(1, 3, -7, 9)