from tkinter import *

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
    save = Button(win, text = "SAVE", command = lambda: save_contents(Days, course_name, Times))
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

def save_contents(Days, course_name, Times):
    name_c = course_name.get()
    course_name.set('Enter Class Name')
    print(name_c)
    day_list = [ ]
    for key, value in Days.items():
        state = value.get()
        if state != 0:
            day_list.append(key)
            Days[key].set(0)

    (time_1, time_2) = Times

    time_start = time_1.get()
    time_1.set('8:00')

    time_end = time_2.get()
    time_2.set('12:00')

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
    print(time_list)


    print("Start:", time_start)
    print("End:", time_end)
    print(day_list)

    course = (name_c, time_list, day_list)
    return course
    
def clear_contents(Days, course_name, Times):
    course_name.set('Enter Class Name')
    (time_1, time_2) = Times
    time_1.set('8:00')
    time_2.set('12:00')
    for key, value in Days.items():
        Days[key].set(0)
    
    
