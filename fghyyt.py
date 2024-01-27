import pyautogui
g = input('Введите свой логин')
f = input('Введите свой пароль')
while g == 'dodo' and f == 'pizza':
    if g != "dodo":
        print('Неправильный логин')
        g = input('Попробуйте еще раз')
    if f != "pizza":
        print('Неправильный пароль')
        g = input('Попробуйте еще раз')
print('Вход успешно выполнен')
    

