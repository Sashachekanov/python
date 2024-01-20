m1 = int(input(''))
m2 = int(input(''))
m3 = int(input(''))
m4 = int(input(''))
m5 = int(input(''))
m6 = int(input(''))
m7 = int(input(''))
m8 = int(input(''))
m9 = int(input(''))
m10 = int(input(''))
if m1 + m2 + m3 + m4 + m5 > m6 + m7 + m8 + m9 + m10:
    if m6 + m7 > m8 + m9:
        if m9 > m8:
            print('8 монета фальшивая')
        else:
            print('9 монета фальшивая')
    elif m6 + m7 < m8 + m9:
        if m6 > m7:
            print('7 монета фальшивая')
        else:
            print('6 монета фальшивая')
    else:
        print('10 монета фальшивая')
if m1 + m2 + m3 + m4 + m5 < m6 + m7 + m8 + m9 + m10:
    if m1 + m2 > m3 + m4:
        if m3 > m4:
            print('4 монета фальшивая')
        else:
            print('3 монета фальшивая')
    elif m1 + m2 < m3 + m4:
        if m1 > m2:
            print('2 монета фальшивая')
        else:
            print('1 монета фальшивая')
    else:
        print('5 монета фальшивая')