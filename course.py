import random


class Course:
    """
    Will initialize a class using the following format for info:
    info = ( "course name", [start time, end time], [days], color=)

    >>> course = Course(("ECE 212", [8, 9], ["Monday", "Wednesday", "Friday"]))
    >>> course.name == "ECE 212"
    True
    >>> course.start
    8
    >>> course.end
    9
    >>> course.days
    ['Monday', 'Wednesday', 'Friday']
    >>> course.each_day()
    [('Monday', 8, 9), ('Wednesday', 8, 9), ('Friday', 8, 9)]
    """

    # create an empty list, will contain all
    # instances of Course objects
    _instances = []

    def __init__(self, info, color = None):
        """
        Initialize an instance of a Course object
        """
        self.name = info[0]
        times = info[1]
        self.start = times[0]
        self.end = times[1]
        self.days = info[2]
        # color will only be None if it is not
        # a homework type Course object
        if color != None:
            self.color = color
        else:
            self.color = color_rand()

        # insert into collection of instances
        Course._instances.append(self)

    def get_name(self):
        """
        Returns the name of the course
        """
        return self.name

    def get_days(self):
        """
        Returns a list of all days of the course
        """
        return self.days

    def get_start_time(self):
        """
        Returns start time of course
        """
        return self.start
    
    def get_end_time(self):
        """
        Returns end time of course
        """
        return self.end
    
    def get_color(self):
        """
        Returns the color of the object
        """
        return self.color

    def get_all_instances():
        """
        Gets all instances of Course class, allows
        for you to be able to find all possible
        courses in current schedule
        """
        return [i for i in Course._instances]

    def del_instances(self):
        """
        Deletes all instances of the same name,
        but not necessarily the same object handler. 
        Returns NONE
        """
        for i in Course.get_all_instances():
            if i.name == self.name:
                Course._instances.remove(i)
   

    def change_time(self, start, end):
        """
        Change the time to a new (start,end) pair
        >>> course = Course(("ECE 212", [8, 9], ["Monday", "Wednesday", "Friday"]))
        >>> course.change_time("9:00","10:00")
        >>> course.start
        '9:00'
        >>> course.end
        '10:00'
        
        """
        self.start = start
        self.end = end

    def change_days(self, deleted, added):
        """
        Modifies the days of each course, used to edit an
        already existing course.
        [deleted] should be a list of days you want removed
        [added] should be a list of days you want added
        If you only wish to add or delete, simply leave the other list blank ( [] )

        >>> course = Course(("ECE 212", ["8:00", "9:00"], ["Monday", "Wednesday", "Friday"]))
        >>> course.change_days(["Monday","Friday", "Wednesday"], ["Tuesday", "Thursday"])
        >>> course.days
        ['Tuesday', 'Thursday']
        """
        for i in added:
            self.days.append(i)
        
        for i in deleted:
            if i in self.days:
                self.days.remove(i)

    def each_day(self):
        """
        Returns a list of lists, each entry containing a
        compact list with the day, start and end times

        >>> course = Course(("ECE 212", ["8:00", "9:00"], ["Monday", "Wednesday", "Friday"]))
        >>> course.each_day()
        [('Monday', '8:00', '9:00'), ('Wednesday', '8:00', '9:00'), ('Friday', '8:00', '9:00')]
        """
        per_day = []
        for i in self.days:
            per_day.append((i, self.start, self.end))
        return per_day

def get_all_times():
    """
    Returns a dictionary with the days of
    the week as keys and the total amount
    of time used in that day as the value.
    Used in the homework algorithm to 
    determine what day is best to place 
    homework assignments.
    """
    all_courses = Course.get_all_instances()
    days_of_week = {'Sunday': 0, 'Monday': 0, 'Tuesday': 0, 'Wednesday': 0, 'Thursday': 0, 'Friday': 0, 'Saturday': 0}
    courses = []
    # removes all possible duplicate instances for calculation
    for j in all_courses:
        if j not in courses:
            courses.append(j)

    # calculates the time of each course for each day of the week,
    # and keeps a running total
    for i in courses:
        for j in i.days:
            days_of_week[j] = days_of_week[j] + (i.end-i.start)
    # returns a dictionary with the values as total occupied
    # time in that day
    return days_of_week
            
def color_rand():
	"""
	This function creates a random color and returns it in the form
	#rgb wher r,g and b are a hexidecimal value from 0 to f
	"""
	r = str(hex(random.randint(1,16))[2])
	g = str(hex(random.randint(1,16))[2])
	b = str(hex(random.randint(1,16))[2])

	return '#'+r+g+b

def save():
    """
    Saves all objects that exist as instances of a Course
    object. Called whenever you wish to save.
    """

    # retrieve all instances of courses to save
    courses = Course.get_all_instances()
    saved = []
    opened = open("save.txt", 'w')
    # remove duplicates (because an instance saves per day of class)
    for j in courses:
        if j not in saved:
            saved.append(j)
    for i in saved:
        # save in specific format for reloading, saves
        # a course object per line
        st_start = str(i.start)
        st_end = str(i.end)
        opened.write(i.name)
        opened.write(': ')
        opened.write(st_start)
        opened.write(' ')
        opened.write(st_end)
        opened.write(': ')
        for x in i.days:
            opened.write(x)
            opened.write(' ')
        opened.write(':')
        opened.write(str(i.color))
        opened.write(':')
        opened.write('\n')
    #close file, saves memory
    opened.close()
            
def load():
    """
    Loads from a text file as many previously used
    instances of a course as are contained in the text file.
    This is done on startup to recreate the environment
    from previous shutdown.
    
    """
    opened = open("save.txt", 'r')
    # read through all lines of the file (one course per
    # line)
    all_courses = opened.readlines()
    # due to specific format of saving, load back in
    for i in all_courses:
        i = i.split(':')
        name = i[0]
        times = i[1]
        times = times.split()
        times[0] = float(times[0])
        times[1] = float(times[1])
        days = i[2]
        days = days.split()
        Course((i[0], times, days), color=i[3])

        

if __name__ == "__main__":
    import doctest
    doctest.testmod()

