items = [0, None, 0.0, True, 0, 7] # True, 7
found = False
for item in items:
    print('scanning item', item)
    if item:
        found = True
        break

if found:
    print('At least on item evaluates to True')
else:
    print('All items evalute to False')