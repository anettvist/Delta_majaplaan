import PySimpleGUI as sg
from PIL import Image
import io, os

def move_center(window):
    screen_width, screen_height = window.get_screen_dimensions()
    win_width, win_height = window.size
    x, y = (screen_width - win_width)//2, (screen_height - win_height)// 2
    window.move(x, y)

#Stiil
sg.theme('LightGreen10') #värv
sg.theme_input_text_color('white')

layout = [
[sg.Text('Sisesta ruumi number, mida otsid.\nKärgede otsimiseks sisesta kärje täht.\nVetsude otsimiseks sisesta korruse number.', size=(40,4), key='arvuti_tekst')],
[sg.Image(key='pilt')],
[sg.Text('', key = 'pildi_tekst')],
[sg.Input(key='sisestatud_tekst')],
[sg.Button('Otsi'), sg.Button('Tagasi', visible = False), sg.Button('Lõpeta')]]

aken = sg.Window('Majaplaan', layout, margins=(50, 20), keep_on_top=True, no_titlebar=True, grab_anywhere=True)

while True:
    sündmus, väärtused = aken.read()
    
    
    if sündmus == sg.WIN_CLOSED or sündmus == 'Lõpeta':
        break
    
    if sündmus == 'Tagasi':
        aken['arvuti_tekst'].update('Sisesta ruumi number, mida otsid.\n Kärgede otsimiseks sisesta kärje täht.\n Vetsude otsimiseks sisesta korruse number.')
        aken['pilt'].update('')
        aken['pildi_tekst'].update('')
        aken['sisestatud_tekst'].update('')
        aken['Tagasi'].update(visible = False)
        aken['Lõpeta'].update(visible = False)
        aken['Otsi'].update(visible = True)
        aken['Lõpeta'].update(visible = True)
        aken['sisestatud_tekst'].update(visible = True)
        
        continue

#         [sg.Text('Sisesta ruumi number, mida otsid.', size=(30,1), key='arvuti_tekst')],
#         [sg.Image(key='pilt')],
#         [sg.Text('', key = 'pildi_tekst')],
#         [sg.Input(key='sisestatud_tekst')],
#         [sg.Button('Otsi'), sg.Button('Tagasi', visible = False), sg.Button('Lõpeta')]
    
    aken['sisestatud_tekst'].update('')
    
    faili_nimi = str(väärtused['sisestatud_tekst'].upper()) + '.jpg'
    
        
    #Kui soovitakse ruumi otsida ja selline fail eksisteerib
    if sündmus == 'Otsi' and os.path.exists(faili_nimi):
        
        image = Image.open(faili_nimi)
        #Määrab ära pildi suuruse pikslites
        image.thumbnail((500, 500))
        #Loob RAM'i koha, kuhu me saame pildi salvestada
        bio = io.BytesIO()
        #Salvestab pildi
        image.save(bio, format='PNG')
        
        aken['arvuti_tekst'].update(f"Ruum {väärtused['sisestatud_tekst'].upper()} asub siin.")
        #aken['pildi_tekst'].update('Järgmise ruumi otsimiseks sisesta ruumi number.')
        aken['pilt'].update(data=bio.getvalue())
        aken['Tagasi'].update(visible = True)
        aken['Otsi'].update(visible = False)
        aken['sisestatud_tekst'].update(visible = False)
        
        move_center(aken)
        
        continue
        
    else:
        aken['pilt'].update('')
        aken['arvuti_tekst'].update(f"Sellist ruumi ei leitud.")
        #aken['pildi_tekst'].update('Proovi uuesti või otsi mõnda teist ruumi.')
        aken['Tagasi'].update(visible = True)
        aken['Otsi'].update(visible = False)
        aken['sisestatud_tekst'].update(visible = False)
        
        move_center(aken)
        
        continue


aken.close()