from random import randint
from num2words import num2words
from gtts import gTTS
from mpyg321.MPyg123Player import MPyg123Player
import os
import numpy as np
import tkinter as tk

language = 'ja'

main_bg = '#D9CBA9'
number_fg = '#666D4C'
kanji_fg = '#D77064'
label_bg = main_bg

def number_in_japanese(number):
    return num2words(number, lang='ja')

def on_button_click():
    min_number = 0
    max_number = 10000
    random_number = randint(min_number,max_number)
    number_label.config(text=f"{random_number}")
    
def on_show_btn_click():
    number = number_label.cget('text')
    kanji = number_in_japanese(number)
    kanji_label.config(text=kanji)

def on_say_btn_click():
    number = number_label.cget('text')
    number_in_ja = number_in_japanese(number)
    speech = gTTS(text=number_in_ja, lang=language, slow=True)
    speech.save('output.mp3')
    os.system(r'mpg123 output.mp3')

# Create the main window
window = tk.Tk()
window.title("Japanese Numbers Quiz")

# Get screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Set the window dimensions
width = 400
height = 400

# Calculate the x and y coordinates to center the window
x = (screen_width - width) // 2
y = (screen_height - height) // 2

window.geometry(f"{width}x{height}+{x}+{y}")
window['bg'] = main_bg

# Number Label
number_label = tk.Label(window, text="", fg=number_fg, bg=label_bg, font=('Arial',36))
number_label.pack(pady=10)

# Kanji Label
kanji_label = tk.Label(window, text="",fg=kanji_fg, bg=label_bg, font=('Arial',36))
kanji_label.pack(anchor='center', pady=10)

# Test Me Button
button = tk.Button(window, text="Test Me!", command=on_button_click)
button.pack(pady=10)

# Show Answer Button
show_button = tk.Button(window, text='Show Answer', command=on_show_btn_click)
show_button.pack(pady=10)

# Play Button
play_icon = tk.PhotoImage(file=r'play_icon.png')
play_icon = play_icon.subsample(10, 10) 
play_button = tk.Button(window, image=play_icon, command=on_say_btn_click, bg=main_bg, relief=tk.FLAT)
play_button.pack(pady=10)

# Run the Tkinter event loop
window.mainloop()
