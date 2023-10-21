gdspothonny = int(input("Введите вашу темптературу"))
if gdspothonny > 25:
    print("слшкм жр")
    print("Оптимальная темптература на (gdspothonny - 25) хлоднее")
elif gdspothonny < 20:
    print("Слишком холодно")
    print("Оптимальная темптература на (20 - gdspothonny) холоднее")
else:
    print("Приятного отдыха!")