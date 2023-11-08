import PySimpleGUI as sg
from random import randint
import back


sg.theme('Black')


def front():
    flayout = [
        [sg.Text('Bem Vindo')],
        [sg.Button('Entrar'), sg.Button('Sair')]

    ]

    window = sg.Window('To do List', flayout, size=(500, 100), element_justification='center')
    button, values = window.read()
    
    if button == 'Entrar':
        window.close()
    elif button == 'Sair':
        exit()

ID = ''
NAME = back.read_task()

layout = [
    [sg.Text('Nome', font=('Helvetica 14')), sg.InputText('', key='-NAME-', size=(20, 1)),
     sg.Button('Adicionar', button_color=('white', 'green'))],
    [sg.Text('')],
    [sg.Text('Lista', font=('Arial 14'))],
    [sg.Listbox(values=[], size=(40, 6), key='-BOX-', select_mode=sg.LISTBOX_SELECT_MODE_EXTENDED)],
    [sg.Button('Deletar', button_color=('white', 'red')), sg.Button('Sair', button_color=('white', 'blue'))]
]


front()

window = sg.Window('Main Page', layout)

while True:
    button, values = window.read()
    if button == 'Adicionar':
        ID = randint (1, 999)
        NAME = values['-NAME-'].capitalize()

        if NAME != '':
            back.write(ID,NAME)

        NAME = back.read_task()    

        window.find_element('-NAME-').Update('')
        window.find_element('-BOX-').Update(NAME)

    if button == 'Deletar':
        if NAME:
            x = values['-BOX-'][0]
            back.delete(x)
            NAME = back.read_task()
            window.find_element('-BOX-').Update(NAME)

    if button == 'Sair':
        window.close()
        break

    if button == sg.WIN_CLOSED:
        window.close()
        break
    

    







   

    