"""
This is the file that containes all of the code for the main interface 
"""

from tkinter import *
from tkinter import ttk
root = Tk()

#Global Variables
global canvas_width
global canvas_height
global number_of_days
global hours_in_day

canvas_width = 600
canvas_height = 400
number_of_days = 7
hours_in_day = 10

# Buttons we will ned
create_new = ttk.Button(root, text='New Appointment', padding=(5,5,5,5))

# Make frame to hold our canvas
frame = ttk.Frame(root, relief = "sunken", borderwidth = 5, padding=(3,3,3,3))

# Set up our Canvas
canvas = Canvas(frame, width = canvas_width, height=canvas_height)

#A loop to create a grid
for i in range(0,canvas_height+1, canvas_height//hours_in_day):
	canvas.create_line(0, i, canvas_width, i, tags=('grid', 'HorizontalLines'))
for i in range(0,canvas_width+1,canvas_width//number_of_days):
	canvas.create_line(i, 0, i, canvas_height, tags =('grid', 'VirticleLines'))

#grid all widgets
frame.grid(column = 1, row = 1, columnspan = 7, rowspan= 10) 
canvas.grid()
create_new.grid(column= 0, row=0)
root.mainloop()	