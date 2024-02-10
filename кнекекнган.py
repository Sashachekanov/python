i = input('Jaja')
sima = 0
n = 0
while i != 'стоп':
    i = input('Введите оценку')
    
    if i != 'стоп':
        sima += int(i)
        n = n + 1
print(sima / n)
           
