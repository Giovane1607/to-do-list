import PySimpleGUI as sg
from random import randint
import back


sg.theme('LightBrown')


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
    [sg.Text('Coloque os seus afazeres'), sg.InputText('', key='-NAME-')],
    [sg.Button('Adicionar')],
    [sg.Text('')],
    [sg.Text('Lista')],
    [sg.Listbox(NAME, size=(50,10), key='-BOX-')],
    [sg.Button('Deletar'), sg.Button('Sair')]
    
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







   

    