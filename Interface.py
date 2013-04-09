"""
This is the file that containes all of the code for the main interface 
"""
from tkinter import *
from tkinter import ttk
import random

#Global Variables
global grid_col_max
global grid_row_max
global appointment_editor
global number_of_days
global hours_in_day
global schedule
global days_of_week
global root


root = Tk()
grid_col_max=8
grid_row_max=10
schedule = {}
frame_column = 1
frame_row = 1
number_of_days = 7
hours_in_day = 10
days_of_week = ['Sunday','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
appointment_editor = None

class ScheduleFrame():

	def __init__(self, parent, Borderwidth, Relief, start_time, end_time ,day):
		"""
		Initializes the frame
		There are many more arguments that COULD be passed to a frame initializer 
		but these will do for this specific application. Technically since this is a class 
		with a very specific task, I could have probably hardcoded all the arguments, minus the parent.
		This way however, is slightly more modular 

		"""
		#initialize the TK frame with the values we want
		self._frame = ttk.Frame(parent, borderwidth=Borderwidth, relief=Relief)
		self._borderwidth = Borderwidth
		self._course = None
		self._color = None
		self._start_time = start_time
		self._end_time = end_time
		self._day = day
		self._tophalf = None
		self._bottomhalf = None

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
		"""
		This method allows special functions to be binded to each frame 
		"""
		self._frame.bind(event, function)
	def appointmentEditor(self, event):
		"""
		This funciton calles the appointment editor. If one is currently open 
		it will destroy the currently open editor and create a new one.
		"""
		#this should be replaced by the caller to Brittany's code 
		#find a better solution than putting it twice? 
		global appointment_editor
		if appointment_editor == None:
			appointment_editor = Toplevel(root)
		else:
			appointment_editor.destroy()
			appointment_editor = Toplevel(root)
	def markBusy(self, class_name, color):
		"""
		This functions fills in the frame if an appointment is added. If the appointment ends on the half hour in this frame
		it will fill the top half. If an appointment starts in this frame it will fill the bottom half.  
		"""
		global schedule

		#Fill the frame with a random color if one is not provided 
		if color == None:
			r = str(hex(random.randint(0,16)))
			g = str(hex(random.randint(0,16)))
			b = str(hex(random.randint(0,16)))
			self._color = '#'+r+g+b
		else:									#otherwise we use the color provided
			self._color = color

		#appointment ends on the hour, fill the whole frame
		if self._tophalf == None and self._bottomhalf == None:	
			self._frame.configure(background=color)
			self._frame.Label(text = class_name).grid(sticky = 'news')

		#appointment ends or begins on half hour
		else:

			#appointments ends in this frame
			if self._course._endtime <= self._endtime:
				self._tophalf.configure(background=color)
				self._tophalf.Label(text = class_name).grid(sticky = 'news')

			#appointment begins in this frame	
			else:
				self._bottomhalf.configure(background=color)
				self._bottomhalf.Label(text = class_name).grid(sticky = 'news')

		#recursive call to the funciton if the appointment spans multiple frames
		if self._course._endtime > self._endtime:
				for i in schedule[self._day]:
					if i._start_time == self._endtime:
						i.markBusy(class_name, self._color)
	def markAvailable(self):
		 """
		 This function resets the color in the frame when an appointment is removed
		 """
		 global schedule

		 color = 'grey'
		 if self._tophalf == None and self._bottomhalf == None:	
			self._frame.configure(background=color)
			self._frame.

	def split(self):
		"""
		If an appointment is added that goes on the half hour we have to split the frame
		"""
		#set up the frame to be resizeable
		self._frame.columnconfigure(0, weight = 1, minsize = 70)
		for i in (0,1):
			self._frame.rowconfigure(i, weight=1, minsize=25)

		#Put two smaller frames in the schedule frame and set options
		self._tophalf = ttk.Frame(self._frame, relief='solid', borderwidth = 1).grid(row = 0, column = 0)
		self._bottomhalf = ttk.Frame(self._frame, relief='solid', borderwidth = 1).gird(row = 1, column=0)

		#Have to bind the appropiate functions to the top and bottom half of the frame now
		for i in (self._tophalf, self._bottomhalf):
			i.bind('<Enter>', frame.hover)
			i.bind('<Leave>', frame.leave)
			i.bind('<Double-Button-1>', frame.appointmentEditor)

	def destroySplit(self):
		"""
		If we no longer need the frame to be split, this can be called to destroy the split
		"""
		self._tophalf.forget()
		self._bottomhalf.forget()

		self._tophalf = None
		self._bottomhalf = None



# ***THIS IS A DUMBY FUNCTION TO OPEN ANOTHER WINDOW***
#this will be replaced by the caller to Brittany's code	
def appointmentEditor():
	"""
	This funciton calles the appointment editor. If one is currently open 
	it will destroy the currently open editor and create a new one.
	"""
	global appointment_editor
	if appointment_editor == None:
		appointment_editor = Toplevel(root)
	else:
		appointment_editor.destroy()
		appointment_editor = Toplevel(root)

# Buttons we will need

#This is to create a new appointment
create_new = ttk.Button(root, text='New Appointment', padding=(5,5,5,5), command=appointmentEditor)


#A loop to create a grid of frames (our shedule)

for i in range(number_of_days):
	ttk.Label(text=str(days_of_week[i])).grid(row = 0, column = i+1)			#create the day Labels
	for j in range(hours_in_day):

		#Create a frame for every hour of every day"

		frame = ScheduleFrame(root, 1, 'solid', j+8, j+9, days_of_week[i])
		frame.grid('nwes', j+1, i+1)

		#Bind all the functions we want to each frame
		frame.bind('<Enter>', frame.hover)
		frame.bind('<Leave>', frame.leave)
		frame.bind('<Double-Button-1>', frame.appointmentEditor)
		

		#Put all the frames in a dictionary so we can access them later 
		#to add appointments 
		
		if days_of_week[i] not in schedule:
			schedule[days_of_week[i]] = set()
			schedule[days_of_week[i]].add(frame)
		else:
			schedule[days_of_week[i]].add(frame)

#This loop prints the labels (time of day) along the left side of the schedule 
for i in range(hours_in_day):
	ttk.Label(text=str(i+8)+':00').grid(column=0, row=i+1)		

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