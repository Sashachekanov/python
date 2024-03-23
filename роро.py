list1 = ['*', '|', '#', '#', '|','#','#','|','#','#']
for i in range(20):
    print(list1.index('*'))
    k = (list1.index('*'))
    q = (list1.index('*'))
    g = input('право или лево?, прыжок право или прыжок лево?')
    if g == 'право':
        q = q + 1
        if list1[q] == '|':
            print('лошара в стену попал')

        elif:
            list1[k] = '#'
            k = k + 1
            if k > 9:
                k = k - 1
            list1[k] = '*'


    elif g == 'лево':
        list1[k] = '#'
        k = k - 1
        if k < 0:
            k = k + 1
        list1[k] = '*'
    print(*list1)