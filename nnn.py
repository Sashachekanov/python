n = 0
list1 = ['g','t','d','r','b']
for i in range(5):
    h = list1[n]
    print(list1[n])
    k = input('Удалить или заменить?')
    if k == 'удал':
        list1.remove(h)
        n = n - 1

    if k == 'замен':
        g = input('koool')
        list1[i] = g
    n = n + 1


print(list1)



