import PySimpleGUI as sg
import tkinter as tk

# Define a function to set different fonts for different parts of the text
def apply_fonts(widget, text, fonts):
    start = 0
    for font, length in fonts:
        widget.tag_configure(font, font=(font,))
        widget.insert("end", text[start:start+length], font)
        start += length

# Create a layout with a multiline text element
layout = [
    [sg.Multiline(size=(40, 10), key='-TEXTBOX-', font=('Helvetica', 12))]
]

window = sg.Window('Text with Multiple Fonts', layout, finalize=True)

# Access the tkinter Text widget element
text_widget = window['-TEXTBOX-'].Widget

# Define the text and fonts for different parts
text = "This is some text with multiple fonts"
fonts = [('Helvetica', 4), ('Courier', 10), ('Arial', 4)]

# Apply the fonts to the text widget
apply_fonts(text_widget, text, fonts)

# Event loop
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break

window.close()
