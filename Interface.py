"""
CMPUT 297/115 - Final Project - Due 2013-04-12

    Version 1.0 2013-04-12

    By: Cody Otto
        Brittany Lamorie
        Ryan Thornhill

    This assignment has been done under the full collaboration model,
    and any extra resources are cited in the code below.

    This is the file that containes all of the code for the main interface 
    and the toplevel windows called by the two buttons on the left hand side
    of the main interface.

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
grid_row_max=11
schedule = {}
frame_column = 1
frame_row = 2
number_of_days = 7
hours_in_day = 10
days_of_week = ['Sunday','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
appointment_editor = None

#------------------------------------------------Schedule Frame Class-------------------------------------------------

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
		self._topname = None
		self._bottomname = None
		self._name_appt = "Enter Class Name"
		parent.title(string= "Schedule Builder")


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

		#reset the background color 
		color = 'white'

		#Fill the whole frame
		if top == False and bottom == False:
			for i in self._frame.grid_slaves():
				i.destroy()
			self._frame.configure(background=color)

		#Just fill the top
		if top == True:
			#destory all frames inside main frame
			for i in self._tophalf.grid_slaves():
				i.destroy()

			#reset the labels
			self._topname = False
			self._tophalf_busy = False
			self._name_appt = self._bottomname.cget('text')
			self._tophalf.configure(background=color)

		#Just fill the bottom
		if bottom == True:
			#Destroy all frames inside main frame
			for i in self._bottomhalf.grid_slaves():
				i.destroy()
			#Reset all labels
			self._bottomname = False
			self._bottomhalf_busy = False
			self._name_appt = self._topname.cget('text')
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

		#Set resize options 
		self._tophalf.columnconfigure(0, minsize=70, weight=1)
		self._tophalf.rowconfigure(0, minsize=25, weight=1)
		self._bottomhalf.columnconfigure(0, minsize=70, weight=1)
		self._bottomhalf.rowconfigure(0, minsize=25, weight=1)


	def destroySplit(self):
		"""
		If we no longer need the frame to be split, this can be called to destroy the split
		"""
		#Destory everythin inside the main frame
		for w in self._frame.grid_slaves():
			w.destroy()

		#Reset all possible labels that could have been set
		self._name = False
		self._name_appt = None
		self._topname = False
		self._bottomname = False
		self._tophalf_busy = False
		self._bottomhalf_busy = False
#------------------------------------------------Appointment Editor---------------------------------------------------

def MenuWin(name_c, time_list, day_list):
    """
	Initializes the toplevel menu window, calling each seperate function to create the 
    widgets on the menu. 
    """
    win = Toplevel()
    #Add a title to the window
    win.title(string= "Class Editor")
    menu_ttl = Label(win, text = "Course Information")
    menu_ttl.grid(column=1, row=0, pady=5)
    course_name = Course_Input(win, name_c)
    Days = set_days(win, day_list)
    Times = set_times(win, time_list)
    #Create buttons for saving, deleting and clearing the widgets
    save = Button(win, text = "SAVE", command = lambda: save_contents(course_name, Times, Days))
    save.grid(column=5, row=6) 
    clear = Button(win, text = "CLEAR", command = lambda: clear_contents(Days, course_name, Times))
    clear.grid(column=3, row=6)
    delete =  Button(win, text = "DELETE", command = lambda: delete_contents(Days, course_name, Times) )
    delete.grid(column=2, row=6)

def HW_win():
    """
    Creates another toplevel menu window used to add assignments to the schedule
    this function call similar functions to the initial menu window create the widgets 
    for this menu.
    """
    HW = Toplevel()
    #Add a title to the window
    HW.title(string= "Homework Assignment")
    HW_ttl = Label(HW, text = "Assignment Information")
    HW_ttl.grid(column=1, row=0, pady=5)
    HW_name = Course_Input(HW, "Enter Assignment Title")
    HW_due = set_days(HW, [ ])
    #Assign a variable to the contents of the option menu
    HW_time = StringVar()
    HW_time_Lab = Label(HW, text = "Approximate Time for Completion(In hours)")
    HW_time_Lab.grid(column=0, row=5, columnspan=2)
    HW_time_sel = OptionMenu(HW, HW_time, '1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
    HW_time_sel.grid(column=2, row=5) #A different option menu was created for this window so that the hours to completion could be saved
    save = Button(HW, text = "SAVE", command = lambda: Calc_HW(HW_name, HW_time, HW_due))
    save.grid(column=5, row=6)

def Course_Input(win, title):
    """
    This function creates the input widget on each menu and label on each menu.
    It return the string variable containing the name of the course or assignment
    """
    name = Label(win, text = "Name:")
    name.grid(column=0, row=2)
    enter = Entry(win, relief = 'sunken')
    #Assigns a variable to the contents of the entry widget
    course = StringVar()
    course.set(title)
    enter["textvariable"] = course
    enter.grid(column=1, row=2)

    return course

def set_days(win, day_list):
    """
    Creates the checkbutton widgets on both menus. It returns the dictionary
    of Days of the week with the state of each check button as it's items.
    """
    #Create a dictionary for the days of the week and the state of the corresponding checkbutton
    Days = {
        'Sunday':0,
        'Monday':0,
        'Tuesday':0,
        'Wednesday':0,
        'Thursday':0,
        'Friday':0,
        'Sunday':0
        }
            
    #The list is used to label the check buttons in proper order
    List_Days = [ 'Sunday','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    counter=0 
    for key in List_Days:
        #Initialize the item of each day as the checkbutton variable
        Days[key] = IntVar()
        if key in day_list:
            #When the frame is double clicked to open a menu the day is sent to
            #this function so that the menu is set to the proper day
            Days[key].set(1)
        CheckBox = Checkbutton(win, text = key, variable = Days[key])
        CheckBox.grid(column=counter, row=3)
        #Counter is used to unpack the checkbuttons in order, without over lap
        counter = counter + 1

    return Days

def set_times(win, time_list):
    """
    Creates the option menus for start and end times of the courses added. Returns a tuple containing
    both start and end time variables.
    """
    (start_time, end_time) = time_list
    #Set the variables of the option menu
    time_1 = StringVar()
    time_1.set(start_time)
    start = Label(win, text = "Enter Start Time:")
    start.grid(column=0, row=4)
    #Creates a widget for the start times
    time_start = OptionMenu(win, time_1, '8:30', '9:00', '9:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00', '17:30')
    time_start.grid(column=1, row=4)

    #Set the variables of the option menu
    time_2 = StringVar()
    time_2.set(end_time)
    end = Label(win, text = "Enter End Time:")
    end.grid(column=0, row=5)
    #Creates a widget for the start times
    time_end = OptionMenu(win, time_2, '8:00', '8:30', '9:00', '9:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00')
    time_end.grid(column=1, row=5)

    time_list = (time_1, time_2)
    
    return time_list

def get_contents(course_name, Times, Days):
    """
    Retrieves variable values from each set of widgets on
    the course menu. The time values are originally strings
    but are used as floats in other functions, the conversion to
    proper format is found here. Returns a string for the name
    of the course, a tuple of floats for the times and a list of
    strings for the days.
    """
    name_c = course_name.get()
    day_list = [ ]
    #Iterates throught the items of the Days dictionary
    for key, value in Days.items():
        #Sets the item as the state of checkbutton
        state = value.get()
        #If the checkbutton is checked, the day is added to the list
        if state != 0:
            day_list.append(key)
            #The checkbutton is then reset
            Days[key].set(0)
    
    (time_1, time_2) = Times
    #The variables from the option menus are retrieved
    time_start = time_1.get()
    time_end = time_2.get()
    #These variables are strings and must be altered before being used
    start = time_start.split(':')
    end = time_end.split(':')
    #Half hours are converted to .5 increments of the whole hour
    if start[1] != '00':
        start = start[0] +'.5'
    else:
        start = start[0]
    if end[1] != '00':
        end = end[0] + '.5'
    else: 
        end = end[0]
    #These strings are now converted to floats
    start = float(start)
    end = float(end)
    time_list = (start, end)
    info = (name_c, time_list, day_list)
    return info
    
def clear_contents(Days, course_name, Times):
    """
    Sets the variable of each widgets on the course menu
    to the original settings.
    """
    course_name.set('Enter Class Name')
    (time_1, time_2) = Times
    #Iterates through the Dictionary unchecking each button
    for key, value in Days.items():
        Days[key].set(0)
    time_1.set('8:00')
    time_2.set('12:00')

def save_contents(course_name, Times, Days):
    """
    Retrieves informationg containing name, day and times, from the function
    get contents. Checks if this day and time is already taken in the 
    schedule, if it is your addition will not be added. Creates a course type
    object using the information from get_contents and puts it visually 
    on the schedule. Also calls save, so that the new object can be saved
    in the text current text file. 
    """
    info = get_contents(course_name, Times, Days)
    for i in course.Course.get_all_instances():
    	if info[1][0] > i.get_start_time() and info[1][0] < i.get_end_time():
            #Checks if the start time to be added is within any of the busy times 
    		for j in info[2]:
    			if j in i.get_days():
    				return None
    	elif info[1][1] > i.get_start_time() and info[1][1] < i.get_end_time():
            #Checks if the end time to be added is within any of the busy times 
    		for j in info[2]:
    			if j in i.get_days():
    				return None
    	elif info[1][0] == i.get_start_time():
            #Checks if the start time to be added is the same as other start times 
    		for j in info[2]:
    			if j in i.get_days():
    				return None
    clear_contents(Days, course_name, Times)
    app = course.Course((info))
    #Adds each day of busy time to the schedule
    for i in app.get_days():
        markBusy(app.get_name(), app.get_start_time(), app.get_end_time(), i, app.get_color())

    course.save()

    
def get_HW(HW_name, HW_time, HW_due):
    """
    Similar to get_contents, used to retrieve the values
    of the widget's variable on the Assignment menu. Because
    of the different option menu, the same get_contents could not
    be used twice.
    """
    name_HW = HW_name.get()
    #Iterate through the dictionary of days to get the checked buttons
    for key, value in HW_due.items():
        state = value.get()
        if state != 0:
            Due_day = key
    #Get the time from the option menu and converts to a float
    hours = HW_time.get()
    hours = float(hours)
    HW_info = (name_HW, hours, Due_day)

    return HW_info
 
def Calc_HW(HW_name, HW_time, HW_due):
    """
    This sets the times and days that the newly entered assignment should be
    completed in. Using the function get_all_times from course to get
    a dictionary of days of the week with the number of busy hours, and finding all
    availble time on the day with the least busy hours, we are able to evenly spread 
    out work throughout the week. Note: This is set up best for weekly assignments.
    """
    (name_HW, hours, Due_day) = get_HW(HW_name, HW_time, HW_due)
    color = course.color_rand()

    while hours:
        Work_time = course.get_all_times()    
        if Due_day in Work_time:
            #So that work on the due date is not set, it is eliminated fromt he dictionary
            Work_time.pop(Due_day)
        (cur_day, time) = min(Work_time.items(), key = lambda x: x[1])
        avail_hours = avail_time(cur_day)
        if avail_hours == [ ]:
            #If the least busy day has no work hours, homework will not be scheduled till ten
            avail_hours = [10.0]
            #This could be made a variable and set by the user
        course.Course((name_HW, [avail_hours[0], avail_hours[0] + .5], [cur_day]), color=color)
        #Each half hour of work is its own object
        markBusy(name_HW, avail_hours[0], avail_hours[0] + .5, cur_day, color)
        hours = hours - .5
        #This also is used to save the assignment objects in the text file
        course.save()

def avail_time(Day):
    """
    Used to find open time on the day passed. Creates a list
    of start and a list of end times and compares the lists. 
    If the time is not in both lists, then there is an open start time.
    Returns a list of available start time on the day passed.
    """
    #Retrieves each instance already saved
    courses = course.Course.get_all_instances()
    time_starts = [ ]
    time_ends = [ ]
    avail_hours = [ ]
    #Iterates through each instance
    for i in courses:
        #CReates lists of instances for the passed day
        if Day in i.days:
            time_starts.append(i.start)
            time_ends.append(i.end)
    #Compares the start and end times to make one list of available start times
    for j in time_ends:
        if j in time_starts: continue
        else:
            avail_hours.append(j)


    return avail_hours
    

def delete_contents(Days, course_name, Times):
	#convert all strings to values we can use!
	info = get_contents(course_name, Times, Days)
	#find the course we are trying to delete
	for i in course.Course.get_all_instances():
		if info[0]==i.get_name():
			course_object = i
			#Delete the course on all days that it happens
			for i in course_object.get_days():
				markAvailable(course_object.get_start_time(), course_object.get_end_time(), i)
				course_object.del_instances()


	
	course.save()
#------------------------------------------------Logic Functions-----------------------------------------------------

def markBusy(class_name, start, end, day, color):
	"""
	This is the function that fills in the frames in the schedule when an appointment
	is created. 

	It is recursively defined function so that it can properl handle half hour increments
	"""
	global schedule

	#initialize variables we use
	duration = end - start
	already_split = True

	if duration > 0:
		for i in schedule[day]:
			# Find the frame that the start time is contained in 
			if start >= i._start_time and start < i._end_time:

				#In order to avoid overwriting half hour frames, we assume every frame is already split into half hours
				#If it's not we change the variable
				if i._tophalf_busy == False and i._bottomhalf_busy == False:
					already_split = False

				#Recursion part
				if duration > 0.5:

					#Case where the whole frame is filled
					if start == i._start_time:
						i.markBusy(class_name, color, False, False)
						markBusy(class_name,start+1, end, day, color)
					#Case where half the frame is filled 
					else:
						if already_split == False:
							i.split()
						i.markBusy(class_name, color, False, True)
						markBusy(class_name, start+0.5, end, day, color)
				#Where the functions breaks recursion
				else:
						#ends on a half hour
						if start == i._start_time:
							if already_split == False: 
								i.split()
							i.markBusy(class_name, color, True, False)

						#begins on a half hour
						else:
							if already_split == False:
								i.split()
							i.markBusy(class_name, color, False, True)

def markAvailable(start, end, day):
	"""
	This is a recursively defined function that takes an appointment start and end time as well as a day
	and clears those sections on the schedule interface.

	When it comes across a block with 2 half hour oppointments it will clear only one. If only one half hour appointment occurs
	in a block then we destory the split and turn the block into a full hour block again.
	"""
	#Variables we need
	global schedule
	duration = end - start

	#We run while the duration is greater than 0
	if duration > 0:
		#Cycle through all of the frames and find the one where the start time occurs 
		for i in schedule[day]:
			if start >= i._start_time and start < i._end_time:
				#Recursive part
				if duration > 0.5:
					if start ==i._start_time:					#Hour long block to clear
						i.markAvailable(False, False)
						markAvailable(start+1, end, day)
					else:
						if i._tophalf_busy == True:				#Clear bottom block 
							i.markAvailable(False, True)
							markAvailable(start + 0.5, end, day)
						else:
							i.destroySplit()					#Restore block and fill entire area
							i.markAvailable(False, False)
							markAvailable(start + 0.5, end, day)
				#Recursion Ends here 
				else:
					if start == i._start_time:					#Cear top blcok
						if i._bottomhalf_busy == True:
							i.markAvailable(True, False)
						else:
							i.destroySplit()					#Restore block and fill entire area
							i.markAvailable(False, False)
					else:
						if i._tophalf_busy == True:				#Clear bottomblock
							i.markAvailable(False, True)
						else:
							i.destroySplit()					#Restore block and fill entire area
							i.markAvailable(False, False)

def appointmentEditor():
	"""
	This funciton calles the appointment editor. If one is currently open 
	it will destroy the currently open editor and create a new one.
	"""
	global appointment_editor
	#If there isn't an appointment editor currently open, open a new one
	if appointment_editor == None:
		MenuWin("Enter Class Name",('8:00', '12:00'), [ ])
	#If there is, destory it and open a new one
	else:
		appointment_editor.destroy()
		appointment_editor = Toplevel(root)

     
def loadText():
	"""
	This function loads in the text file, supposed to be called at the beggining of the program
	"""
	#Define a list the holds all the current elements 
	courses_loaded = []
	#Load all the course from the text file
	course.load()

	#Add all the new loaded appointments to the schedule Interface
	for i in course.Course.get_all_instances():
		if i not in courses_loaded:				#Don't want to add duplicates 
			courses_loaded.append(i)
			for x in i.get_days():				#Have to add a course for each day it runs
				markBusy(i.get_name(), i.get_start_time(), i.get_end_time(), x, i.get_color())

#-----------------------------------------------------Body of Code -------------------------------------------------------------------------

#This is to create a new appointment
create_new = ttk.Button(root, text='New Appointment', padding=(5,5,5,5), command=appointmentEditor)
#This creates a new assignment
HW_Button = ttk.Button(root, text='Add Assignment', padding=(5,5,5,5), command= HW_win)


#A loop to create a grid of frames (our shedule)

for i in range(number_of_days):
	ttk.Label(text=str(days_of_week[i])).grid(row = 1, column = i+1)			#create the day Labels
	for j in range(hours_in_day):

		#Create a frame for every hour of every day"

		frame = ScheduleFrame(root, 1, 'solid', j+8, j+9, days_of_week[i])
		frame.grid('nwes', j+2, i+1)

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
	ttk.Label(text=str(i+8)+':00').grid(column=0, row=i+2)		

#----------------------------------------------Runtime -------------------------------------------------------
#Load in existing appointments 
loadText()
#-----------------------------------------re-size settings-----------------------------------------------

#Loop through all rows and columns and allow them to be resized
for i in range(grid_col_max+1):
	root.columnconfigure(i, weight=1, minsize=70)
for i in range(grid_row_max+1):
	root.rowconfigure(i, weight = 1, minsize = 50)

#------------------------------------------grid all widgets------------------------------------------------

#buttons
create_new.grid(column= 0, row=0)
HW_Button.grid(column=0, row=1)

#Main window
root.title(string='Scheduler')
root.mainloop()	
