n = 0
list1 = ['g','g','d','g','b']
while 'g' in list1:
    i = list1[n]

    if i == 'g':
        list1.remove(i)
        n = n - 1
    n = n + 1 

print(list1)