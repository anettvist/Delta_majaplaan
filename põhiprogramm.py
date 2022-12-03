import PySimpleGUI as sg

sg.theme('Default1') #värv
aken = [[sg.Text('Tere', size=(40,1), key='kasutaja_tekst')],
[sg.Text('Sisesta klassi number, mida otsid', size=(40,1), key='arvuti_tekst')],
[sg.Input(key='sisestatud_tekst')],
[sg.Button('Otsi'), sg.Button('Lõpeta')]]

aken = sg.Window('Vestlus', aknas)

while True:
    sündmus, väärtused = aken.read()
    if sündmus == sg.WIN_CLOSED or sündmus == 'Lõpeta':
        break
    if sündmus == 'Otsi':
        aken['arvuti_tekst'].update('See klassiruum asub siin')
        aken['kasutaja_tekst'].update(väärtused['sisestatud_tekst'])
        aken['sisestatud_tekst'].update('')
        aken.open('sisestatud_tekst'+'.jpg')

#ja nii ongi
aken.close()