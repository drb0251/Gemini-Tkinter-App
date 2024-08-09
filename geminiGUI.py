# Taking my gemini code and creating a GUI using tkinter
import google.generativeai as genai
import os
from tkinter import *
from dotenv import load_dotenv
load_dotenv()
import tkinter as tk
import ttkbootstrap as ttk

GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')


# function for taking a topic input (paragraph_topic) and adding it to a prompt which is passed to the Gemini API:
def generate_blog():
    topic = entry_str.get()
    response = model.generate_content('summarise the following in one paragraph; ' + topic)
    retrieve_blog = response.text
    print(entry_str.get())
    the_box.insert(tk.END, retrieve_blog)

window = ttk.Window(themename = 'journal')
window.title('Gemini 1.5 Flash')
window.geometry('1200x800')

# Style
my_style = ttk.Style()
my_style.configure('my.TButton', font = ('Calibri 26'))

title_label = ttk.Label(window, 
                        text = "Gemini Report Writer", 
                        font=('Calibri', 30))
title_label.pack(padx=20, pady=20)

prompt_label = ttk.Label(window, 
                         text = "Please enter a topic you would like me to summarise, then click 'Generate':",
                         font = 'Calibri 26')
prompt_label.pack(padx = 20, pady = 20)


input_frame = ttk.Frame(master = window)

entry_str = tk.StringVar()

entry = ttk.Entry(master = input_frame, 
                  textvariable = entry_str,
                  font = 'Calibri 26')

# create paragraph button
create_para_button = ttk.Button(master = input_frame, 
                                text = 'Generate',
                                style = "my.TButton",
                                command = generate_blog)

entry.pack(padx=20,pady=20)
create_para_button.pack(padx=20, pady=20)
input_frame.pack(padx=20,pady=20)

# output portion
output_string = tk.StringVar()

# create text box:
the_box = tk.Text(master = window, wrap = WORD, font = 'Calibri 26')
the_box.pack(padx = 50, pady = 50)

window.mainloop()

#output_label = ttk.Label(master = window, text = 'hello', font = 'Calibri 24', textvariable = output_string)
#output_label.pack(side = 'left', padx = 10, pady = 10)

# code to keep prompting for generation of paragraphs...
#keep_writing = True
#while keep_writing:
#    answer = input('Would you like to write a paragraph? (y for yes, anything else for no): ')
#    if answer == 'y':
#        paragraph_topic = input('Please enter a topic: ')
#        print(generate_blog(paragraph_topic))
#    else:
#        keep_writing = False
#        print('Have a good day then human.')
