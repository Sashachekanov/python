import PySimpleGUI as sg
layout = [[sg.Text('Введите два слова')],
          [sg.InputText(int())],
          [sg.InputText(int())],
          [sg.InputText(int())],
          [sg.Button('Ok'), sg.Button('Отмена')]]
window = sg.Window('Соединитель слов', layout)
running = True
while running:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Отмена':
        running = False
    elif event == 'Ok':
        print(int(values[0]) + int(values[1]) + int(values[2]))

window.close()

































