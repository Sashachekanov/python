list1 = ['#', '#', '*', '#', '#']
for i in range(20):
    print(list1.index('*'))
    k = (list1.index('*'))
    g = input('право или лево?')
    if g == 'право':
        list1[k] = '#'
        k = k + 1
        if k > 4:
            k = k - 1
        list1[k] = '*'
    elif g == 'лево':
        list1[k] = '#'
        k = k - 1
        if k < 0:
            k = k + 1
        list1[k] = '*'
    print(*list1)

print(*list1)