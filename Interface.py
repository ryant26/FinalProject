"""
This is the file that containes all of the code for the main interface 
"""

from tkinter import *
from tkinter import ttk
root = Tk()

#Global Variables
global grid_col_max
global grid_row_max
global frame_column
global frame_row
global number_of_days
global hours_in_day
global schedule
global days_of_week

grid_col_max=8
grid_row_max=10
schedule = {}
frame_column = 1
frame_row = 1
number_of_days = 7
hours_in_day = 10
days_of_week = ['Sunday','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

# Buttons we will need

#This is to create a new appointmen
create_new = ttk.Button(root, text='New Appointment', padding=(5,5,5,5))


#A loop to create a grid of frames (our shedule)

for i in range(number_of_days):
	ttk.Label(text=str(days_of_week[i])).grid(row = 0, column = i+1)			#create the day Labels
	for j in range(hours_in_day+1):

		#Create a frame for every hour of every day 
		ttk.Frame(root, relief='solid',  borderwidth = 1).grid(sticky='nwes', column = i+1, row = j+1, columnspan = 1, rowspan = 1)

		#Put all the frames in a dictionary so we can access them later
		schedule[days_of_week[i]]=root.grid_slaves(column=i+1, row=j+1)


#-----------------------------------------re-size settings-----------------------------------------------

for i in range(grid_col_max+1):
	root.columnconfigure(i, weight=1, minsize=70)
for i in range(grid_row_max+1):
	root.rowconfigure(i, weight = 1, minsize = 50)

#------------------------------------------grid all widgets------------------------------------------------
#Frame
#schedule_frame.grid(column = frame_column, row = frame_row, columnspan = 7, rowspan= 10) 

#Size grip
#size_grip.grid(row=8, column = 	13)

#canvas
#canvas.grid()

#button
create_new.grid(column= 0, row=0)

root.mainloop()	