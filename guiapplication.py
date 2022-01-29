
import PySimpleGUI as sg

sg.theme("Reddit")
layout = [
    
    [sg.Text('Sudoku Generator')],
    [sg.Text('What size do you want 4x4(2), 9x9(3)?')],
    [sg.Slider(orientation='h', key='-SIZE-', range=(2,5))],
    [sg.Text('How many batches do you want?')],
    [sg.Input(key='-INPUT-', enable_events=True)],
    [sg.Text('What difficulty do you want?')],
    [sg.Radio('Easy', "Radiobtns", default=True, size=(10,1), k='-R1-'),
     sg.Radio('Medium', "Radiobtns", default=True, size=(10,1), k='-R2-'),
     sg.Radio('Hard', "Radiobtns", default=True, size=(10,1), k='-R3-')],
    [sg.Button('Submit', key = "-SUBMIT-"), sg.Button('Exit', key = "-EXIT-")],
]

window = sg.Window('Canvas test', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == "-SUBMIT-":
        a,b,c,d,e = int(values["-SIZE-"]), values["-INPUT-"],values["-R1-"],values["-R2-"],values["-R3-"]
        print(a, b, c, d, e)
        if c == True:
            _difficulty = "E"
        if d == True:
            _difficulty = "M"
        if e == True:
            _difficulty = "H"

        break
