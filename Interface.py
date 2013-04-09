"""
This is the file that containes all of the code for the main interface 
"""
from tkinter import *
from tkinter import ttk
import random
import course

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

#-----------------------------------------------------------Schedule Frame Class---------------------------------------------------------

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
		self._frame = Frame(parent, borderwidth=Borderwidth, relief=Relief, bg = 'white')
		self._borderwidth = Borderwidth
		self._start_time = start_time
		self._end_time = end_time
		self._day = day
		self._tophalf = None
		self._bottomhalf = None
		self._tophalf_busy = False
		self._bottomhalf_busy = False
		self._name = None
		self._name_appt = None

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
			MenuWin(self._name_appt, (str(self._start_time)+':00', str(self._end_time)+':00'), [self._day])
		else:
			appointment_editor.destroy()
			appointment_editor = Toplevel(root)
	def markBusy(self, class_name, color, top, bottom):
		"""
		This functions fills in the frame if an appointment is added. If the appointment ends on the half hour in this frame
		it will fill the top half. If an appointment starts in this frame it will fill the bottom half.  
		"""

		#appointment ends on the hour, fill the whole frame
		if top == False and bottom == False:	
			self._frame.configure(background=color)
			self._name = ttk.Label(self._frame, text = class_name, background=color)
			self._name.grid(row = 0, column=0)
			#Bind all the functions we want to each frame
			self._name.bind('<Double-Button-1>', self.appointmentEditor)

		#appointment ends or begins on half hour
		elif top == True:

			#appointments ends in this frame
			self._tophalf.configure(background=color)
			self._topname = ttk.Label(self._tophalf, text = class_name, background=color)
			self._tophalf_busy = True
			self._topname.grid(column=0, row=0)
			#Bind all the functions we want to each frame
			self._topname.bind('<Double-Button-1>', self.appointmentEditor)

		#appointment begins in this frame	
		else:
			self._bottomhalf.configure(background=color)
			self._bottomname = ttk.Label(self._bottomhalf, text = class_name, background=color)
			self._bottomhalf_busy = True
			self._bottomname.grid(column=0, row=0)
			#Bind all the functions we want to each frame
			self._bottomname.bind('<Double-Button-1>', self.appointmentEditor)

		self._name_appt = class_name

	def markAvailable(self, top, bottom):
		"""
		This function resets the color in the frame when an appointment is removed
		"""
		global schedule

		color = 'white'
		if top == False and self._bottom == False:
		 self._frame.configure(background=color)

		if top == True:
			self._tophalf.configure(background=color)
		if bottom == True:
			self._bottomhalf.configure(background=color)


	def split(self):
		"""
		If an appointment is added that goes on the half hour we have to split the frame
		"""
		#self._frame.configure(background='yellow')

		#set up the frame to be resizeable
		self._frame.columnconfigure(0, weight = 1, minsize = 70)
		for i in (0,1):
			self._frame.rowconfigure(i, weight=1, minsize=25)

		#Put two smaller frames in the schedule frame and set options
		self._tophalf = Frame(self._frame, relief='solid', borderwidth = 1, background='white')
		self._bottomhalf = Frame(self._frame, relief='solid', borderwidth = 1, background='white')
		self._tophalf.bind('<Double-Button-1>', self.appointmentEditor)
		self._bottomhalf.bind('<Double-Button-1>', self.appointmentEditor)


		#Set up the two split frames to take up half the area of the main frame
		self._tophalf.grid(column=0, row=0, sticky='nsew')
		self._bottomhalf.grid(column=0, row=1, sticky='nsew')
		self._tophalf.columnconfigure(0, minsize=70, weight=1)
		self._tophalf.rowconfigure(0, minsize=25, weight=1)
		self._bottomhalf.columnconfigure(0, minsize=70, weight=1)
		self._bottomhalf.rowconfigure(0, minsize=25, weight=1)


	def destroySplit(self):
		"""
		If we no longer need the frame to be split, this can be called to destroy the split
		"""
		self._tophalf.forget()
		self._bottomhalf.forget()

		self._tophalf = None
		self._bottomhalf = None

#-----------------------------------Appointment Editor---------------------------------------------------

def MenuWin(name_c, time_list, day_list):
    """
Initializes the toplevel menu window, calling each seperate function that
    """
    win = Toplevel()
    win.title(string= "Class Editor")
    menu_ttl = Label(win, text = "Course Information")
    menu_ttl.grid(column=1, row=0, pady=5)
    course_name = Course_Input(win, name_c)
    Days = set_days(win, day_list)
    Times = set_times(win, time_list)
    save = Button(win, text = "SAVE", command = lambda: save_contents(course_name, Times, Days))
    save.grid(column=5, row=6)
    clear = Button(win, text = "CLEAR", command = lambda: clear_contents(Days, course_name, Times))

    clear.grid(column=3, row=6)

def Course_Input(win, title):
    name = Label(win, text = "Course Name:")
    name.grid(column=0, row=2)
    enter = Entry(win, relief = 'sunken')
    course = StringVar()
    course.set(title)
    enter["textvariable"] = course
    enter.grid(column=1, row=2)

    return course

def set_days(win, day_list):
    Days = {
        'Monday':0,
        'Tuesday':0,
        'Wednesday':0,
        'Thursday':0,
        'Friday':0
        }
            

    List_Days = [ 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    counter=0
    for key in List_Days:
        Days[key] = IntVar()
        if key in day_list:
            Days[key].set(1)
        CheckBox = Checkbutton(win, text = key, variable = Days[key])
        CheckBox.grid(column=counter, row=3)
        counter = counter + 1

    return Days

def set_times(win, time_list):
    (start_time, end_time) = time_list
    time_1 = StringVar()
    time_1.set(start_time)
    start = Label(win, text = "Enter Start Time:")
    start.grid(column=0, row=4)

    time_start = OptionMenu(win, time_1, '8:30', '9:00', '9:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', '19:00', '19:30', '20:00', '20:30', '21:00', '21:30', '22:00', '22:30', '23:00', '23:30', '24:00')
    time_start.grid(column=1, row=4)


    time_2 = StringVar()
    time_2.set(end_time)
    end = Label(win, text = "Enter End Time:")
    end.grid(column=0, row=5)
    
    time_end = OptionMenu(win, time_2, '8:00', '8:30', '9:00', '9:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', '19:00', '19:30', '20:00', '20:30', '21:00', '21:30', '22:00', '22:30', '23:00', '23:30', '24:00')
    time_end.grid(column=1, row=5)

    time_list = (time_1, time_2)
    
    return time_list

def save_contents(course_name, Times, Days):
    print("SAVING!!!")
    info = get_contents(course_name, Times, Days)
    clear_contents(Days, course_name, Times)


    return info
    
def get_contents(course_name, Times, Days):
    name_c = course_name.get()
    day_list = [ ]
    for key, value in Days.items():
        state = value.get()
        if state != 0:
            day_list.append(key)
            Days[key].set(0)
    (time_1, time_2) = Times
    time_start = time_1.get()
    time_end = time_2.get()

    start = time_start.split(':')
    end = time_end.split(':')
    if start[1] != '00':
        start = start[0] +'.5'
    else:
        start = start[0]
    if end[1] != '00':
        end = end[0] + '.5'
    else: 
        end = end[0]
    start = float(start)
    end = float(end)
    time_list = (start, end)
    info = (name_c, time_list, day_list)
    return info
    
def clear_contents(Days, course_name, Times):
    course_name.set('Enter Class Name')
    (time_1, time_2) = Times
    time_1.set('8:00')
    time_2.set('12:00')
    for key, value in Days.items():
        Days[key].set(0)

#------------------------------------------------Logic Functions-----------------------------------------------------

def markBusy(class_name, start, end, day, color):
	global schedule

	duration = end - start
	if duration > 0:
		for i in schedule[day]:
			#recursive call to the funciton if the appointment spans multiple frames
			if start >= i._start_time and start < i._end_time:
				if duration > 0.5:
					if start == i._start_time:
						i.markBusy(class_name, color, False, False)
						markBusy(class_name,start+1, end, day, color)
					else:
						i.split()
						i.markBusy(class_name, color, False, True)
						markBusy(class_name, start+0.5, end, day, color)
				else:
						if start == i._start_time: 
							i.split()
							i.markBusy(class_name, color, True, False)
						else:
							i.split()
							i.markBusy(class_name, color, False, True)

def markAvailable(start, end, day):
	global schedule

	duration = end - start
	if duration >0:
		for i in schedule[day]:
			#recursive call to the function to delete the appointment
			if duration > 0.5:
				if start ==i._start_time:
					pass


# ***THIS IS A DUMBY FUNCTION TO OPEN ANOTHER WINDOW***
#this will be replaced by the caller to Brittany's code	
def appointmentEditor():
	"""
	This funciton calles the appointment editor. If one is currently open 
	it will destroy the currently open editor and create a new one.
	"""
	global appointment_editor
	if appointment_editor == None:
		MenuWin("Enter Class Name",('8:00', '12:00'), [ ])
	else:
		appointment_editor.destroy()
		appointment_editor = Toplevel(root)
def loadText():
	"""
	This function loads in the text file, supposed to be called at the beggining of the program
	"""
	course.load()
	for i in course.Course.get_all_instances():
		for j in i:
			r = str(hex(random.randint(0,16))[2])
			g = str(hex(random.randint(0,16))[2])
			b = str(hex(random.randint(0,16))[2])
			color = '#'+r+g+b
			for x in j.get_days():
				markBusy(j.get_name(), j.get_start_time(), j.get_end_time(), x, color)

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

#----------------------------------------------TEST CODE -------------------------------------------------------
"""
This is the test code section because scrolling through all of cody's doctests is probably the most painfull experience of my life
"""
loadText()
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
