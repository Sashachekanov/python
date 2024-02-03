
import os
g = input('Введите команду')
while g != 'стоп':
    g = input('Введите команду')
    if g == 'показать текст':
        m = open('microsoft.txt', 'r')
        o = m.read()
        m.close()
        print(o)
    if g == 'добавить текст':
        m = open('microsoft.txt', 'a')
        f = input('что добавить')
        j = m.write('\n' + f)
        m.close()
    if g == 'открыть':
        os.startfile('microsoft.txt')
    if g == 'заменить текст':
        m = open('microsoft.txt', 'w')
        c = input('что туда поставить')
        m.write(c)
        m.close()
    if g == 'создать новый файл':
        n = input('как будет называться файл?')
        s = open(n, 'w')
        os.path.exists(n)
        
        
        
        
        
        