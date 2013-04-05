"""
This is the file that containes all of the code for the main interface 
"""

from tkinter import *
from tkinter import ttk
root = Tk()

#Global Variables
global canvas_width
global canvas_height
global frame_column
global frame_row
global number_of_days
global hours_in_day

canvas_width = 600
canvas_height = 400
frame_column = 1
frame_row = 1
number_of_days = 7
hours_in_day = 10

# Buttons we will ned
create_new = ttk.Button(root, text='New Appointment', padding=(5,5,5,5))

# Make frame to hold our canvas
schedule_frame = ttk.Frame(root, relief = "sunken", borderwidth = 5, padding=(3,3,3,3))

# Set up our Canvas
#canvas = Canvas(schedule_frame, width = canvas_width, height=canvas_height)

#A loop to create a grid of frames
days_of_week = ['Sunday','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
for i in range(number_of_days):

	ttk.Label(text=str(days_of_week[i])).grid(row = 0, column = i+1)			#create the day Labels

	for j in range(hours_in_day+1):
		ttk.Frame(root, relief='solid', width = 70, height = 50, borderwidth = 1).grid(sticky='nwes', column = i+1, row = j+1, columnspan = 1, rowspan = 1)

#------------------------------------------grid all widgets------------------------------------------------
#Frame
schedule_frame.grid(column = frame_column, row = frame_row, columnspan = 7, rowspan= 10) 

#canvas
#canvas.grid()
#grid
create_new.grid(column= 0, row=0)

root.mainloop()	