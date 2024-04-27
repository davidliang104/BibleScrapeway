import biblescrapeway
from biblescrapeway import query
import PySimpleGUI as sg
import pyperclip

layout = [
    [sg.Input(key='-INPUT-', expand_x=True, focus=True), sg.Button('Search', bind_return_key=True)],
    [sg.Multiline(size=(40, 10), key='-TEXTBOX-', font=('Fira Code', 11))]
]

window = sg.Window('BibleScrapeway', layout)

# Event loop
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == 'Search':
        try:
            search = values['-INPUT-']
            verses = query(search, version = "CSB")

            # add all queried verses to a string
            output = ""
            for verse in verses:
                verse_dict = verse.to_dict()
                verse_no = verse_dict['verse']
                verse_text = verse_dict['text']
                # add space to verse end if there isn't one
                if verse_text.endswith(" ") == False:
                    verse_text = verse_text + ' '
                output += "{} {}".format(verse_no, verse_text)

            # display final string
            window['-TEXTBOX-'].update(output)
            pyperclip.copy(output)
        except Exception as e:
            window['-TEXTBOX-'].update("Invalid input")
        inputBox = window['-INPUT-'].Widget
        inputBox.select_range(0, 'end')
    
window.close()