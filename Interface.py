"""
This is the file that containes all of the code for the main interface 
"""
from tkinter import *
from tkinter import ttk
root = Tk()

#Global Variables
global grid_col_max
global grid_row_max

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

class ScheduleFrame():

	def __init__(self, parent, Borderwidth, Relief):
		"""
		Initializes the frame

		The main reason for this class is to be able to hover the 
		"""
		#initialize the TK frame with the values we want
		self._frame = ttk.Frame(parent, borderwidth=Borderwidth, relief=Relief)
		self._borderwidth = Borderwidth

	def grid(self, Stickey, Row, Column):
		"""
		This method "grids" the frame
		"""
		self._frame.grid(sticky=Stickey, row=Row, column=Column)

	def hover(self, event):
		"""
		When the mouse is hovering the frame we want to "highlight" 
		it by making the boarder thicker.
		"""
		self._frame.configure(borderwidth=self._borderwidth+2)
	def leave(self, event):
		"""
		When the mouse leaves the frame we want to return
		the border to it's original size
		"""
		self._frame.configure(borderwidth=self._borderwidth)
	def bind(self, event, function):
		self._frame.bind(event, function)
	

# Buttons we will need

#This is to create a new appointment
create_new = ttk.Button(root, text='New Appointment', padding=(5,5,5,5))


#A loop to create a grid of frames (our shedule)

for i in range(number_of_days):
	ttk.Label(text=str(days_of_week[i])).grid(row = 0, column = i+1)			#create the day Labels
	for j in range(hours_in_day+1):

		#Create a frame for every hour of every day"
		"""
		frame =  ScheduleFrame
		frame.grid(sticky='nwes', column = i+1, row = j+1)
		"""
		
		#frame = ScheduleFrame(root, 1, 'solid')
		frame = ScheduleFrame(root, 1, 'solid')
		frame.grid('nwes', j+1, i+1)
		frame.bind('<Enter>', frame.hover)
		frame.bind('<Leave>', frame.leave)
		

		#Put all the frames in a dictionary so we can access them later 
		#to add appointments 
		
		if days_of_week[i] not in schedule:
			schedule[days_of_week[i]] = set()
			schedule[days_of_week[i]].add(frame)
		else:
			schedule[days_of_week[i]].add(frame)
		

#-----------------------------------------re-size settings-----------------------------------------------

#Loop through all rows and columns and allow them to be resized
for i in range(grid_col_max+1):
	root.columnconfigure(i, weight=1, minsize=70)
for i in range(grid_row_max+1):
	root.rowconfigure(i, weight = 1, minsize = 50)

#------------------------------------------grid all widgets------------------------------------------------

#button
create_new.grid(column= 0, row=0)

root.mainloop()	