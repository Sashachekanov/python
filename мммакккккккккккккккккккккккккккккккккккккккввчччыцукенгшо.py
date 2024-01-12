g = input('Введите команду')
while g != 'стоп':
    g = input('Введите операцию')
    if g == '+':
        l = int(input('Введите первое число'))
        k = int(input('Введите второе число'))
        print(l + k)
    elif g == '-':
        l = int(input('Введите первое число'))
        k = int(input('Введите второе число'))
        print(l - k)
    elif g == '*':
        l = int(input('Введите первое число'))
        k = int(input('Введите второе число'))
        print(l * k)
    else:
        l = float(input('Введите первое число'))
        k = float(input('Введите второе число'))
        print(l / k)