m = open('microsoft.txt', 'r')
o = (int(m.read()))
m.close()
print(o)
f = input('Что сделать с счётом?, оставить как есть, отнять, прибавить') 
if f == 'отнять':
    
    p = int(input('Сколько отнять?'))
    
    k = open('microsoft.txt', 'w')
    k.write(str(o - p))
    k.close()
    
elif f == 'прибавить':
    
    l = int(input('Сколькo прибавить?'))
    s = open('microsoft.txt', 'w')
    s.write(str(o + l))
    s.close()
else:
    s = open('microsoft.txt', 'w')
    s.close()