g = 20
n = 20
s = 0
q = 0
import random
for i in range(10):
    if g < 1:
        s += 1
        m = open('microsoft.txt', 'w')
        m.write(s,q)
        m.close()
    elif n < 1:
        q += 1
        m = open('microsoft.txt', 'w')
        o = (int(m.writer(s,q)))
        m.close()
    h = input('Команда')
    if h == 'атака':
        k = (random.randint(1,6))
        if k == 1:
            g -= 5
        elif k == 2 or 3:
            g -= 3
        elif k == 4 or 5:
            n -= 3
        elif k == 6:
            n -= 5
    elif h == 'защита':
        m = (random.randint(1,6))
        if m == 6:
            g += 6
            if g > 20:
                g -= 1
                if g > 20:
                    g -= 1
                    if g > 20:
                        g -= 1
                        if g > 20:
                            g -= 1
                            if g > 20:
                                g -= 1
                                if g > 20:
                                    g -= 1
        elif m == 4 or 5:
            g += 6
            if g > 20:
                g -= 1
        elif m == 1:
            g -= 2
            
