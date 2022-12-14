import PySimpleGUI as sg
from PIL import Image
import io, os

sg.theme('Default1') #värv
aken = [[sg.Text('Tere', size=(40,1), key='kasutaja_tekst')],
[sg.Image(key='pilt')],
[sg.Text('Sisesta klassi number, mida otsid', size=(40,1), key='arvuti_tekst')],
[sg.Input(key='sisestatud_tekst')],
[sg.Button('Otsi'), sg.Button('Lõpeta')]]

aken = sg.Window('Vestlus', aken)

while True:
    sündmus, väärtused = aken.read()
    if sündmus == sg.WIN_CLOSED or sündmus == 'Lõpeta':
        break
    if sündmus == 'Otsi':
        aken['arvuti_tekst'].update('See klassiruum asub siin')
        aken['kasutaja_tekst'].update(väärtused['sisestatud_tekst'])
        aken['sisestatud_tekst'].update('')
       
        faili_nimi = str(väärtused['sisestatud_tekst']) + '.jpg'
        
        #Kui selline fail eksisteerib
        if os.path.exists(faili_nimi):
            image = Image.open(faili_nimi)
            #Määrab ära pildi suuruse pikslites
            image.thumbnail((400, 400))
            #Loob RAM'i koha, kuhu me saame pildi salvestada
            bio = io.BytesIO()
            #Salvestab pildi
            image.save(bio, format='PNG')
            aken['pilt'].update(data=bio.getvalue())

aken.close()