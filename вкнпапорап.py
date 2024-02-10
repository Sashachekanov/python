i = input('Jaja')
sima = 0
n = 0
while i != 'стоп':
    i = input('Введите яблоко')
    
    if i != 'стоп':
        i = int(i)
        if i >=200:
            sima += int(i)
            n = n + 1
        elif i <=150:
            sima += int(i)
            n = n + 1
        
print(sima)
print(n)
           
      