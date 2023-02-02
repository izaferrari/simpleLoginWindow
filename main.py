from PySimpleGUI import PySimpleGUI as sg
sg.theme('LightGrey5')
layout = [
    [sg.Text('Usuario'), sg.Input(key='Usuario')],
    [sg.Text('Senha'), sg.Input(key='Senha', password_char='*')],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')]
]
janela = sg.Window('Tela de login', layout)
while True:
    eventos, valores = janela.Read()
    if eventos == sg.WINDOW_CLOSED:
        break
