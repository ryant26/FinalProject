import random


class Course:
    """
    Will initialize a class using the following format for info:
    info = ( "course name", ["start time", "end time"], [days])

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


    _instances = {}

    def __init__(self, info, free = False):
        self.name = info[0]
        times = info[1]
        self.start = times[0]
        self.end = times[1]
        self.days = info[2]
        # assigns True or False for use with
        # homework algorithm, won't factor in
        # free time
        self.free = free

        # insert into collection of instances
        for i in self.days:
            if i in Course._instances:
                Course._instances[i].append(self)
            else:
                Course._instances[i]=[self]

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

    def get_all_instances():
        """
        Gets all instances of Course class, allows
        for you to be able to find all possible
        courses in current schedule
        """
        return [i for i in Course._instances.values()]

    def del_instance(self, i):
        """
        Deletes an instance of Course, specified by object handler.
        If no instance, specifically returns NONE
        """
        if i in self._instances:
            del(Person._instances[i])
        else:
            return None

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
class Homework:
    """
    Defines objects as homework. Very similar to 
    a course object, but it only has a single time
    and it has a due date.
    """
    
    _instances = {}
    
    def __init__(info):
        self.name = info[0]
        self.time = info[1]
        self.date = [info[2]]
        
        for i in self.date:
            if i in Homework._instances:
                Homework._instances[i].append(self)
            else:
                Homework._instances[i]=[self]
    def get_homework_name(self):
        """
        Returns the name of the assignment
        """
        return self.name
    
    def get_due_date(self):
        """
        Returns the due date of the assignment
        """
        return self.date

    def get_assignment_time(self):
        """
        Returns amount of time required
        to do assignment
        """
        return self.time
    def get_all_instances():
        """
        Gets all instances of Course class, allows
        for you to be able to find all possible
        courses in current schedule
        """
        return [i for i in Homework._instances.values()]
def get_all_times():
    """
    Returns a dictionary with the days of
    the week as keys and the total amount
    of time used in that day as the value.
    Used in the homework algorithm to 
    determine what day is best to place 
    homework assignments
    """
    all_courses = Course.get_all_instances()
    all_homework = Homework.get_all_instances()
    days_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    courses = []
    homework = []
    for i in all_courses:
        for j in i:
            if j not in courses:
                courses.append(j)
    for i in all_homework:
        for j in i:
            if j not in homework:
                homework.append(j)
    
    for i in courses

def save_homework():
    """
    Saves all objects of type Homework into
    a text file separate from the storing of
    the courses due to different requirements
    """
    all_homework = Homework.get_all_instances()
    opened = open("save_homework.txt", 'w')
    

def save():
    """
    Saves all objects that exist as instances of a Course
    object. Called whenever you wish to save.
    """

    #retrieve all instances of courses to save
    courses = Course.get_all_instances()
    saved = []
    opened = open("save.txt", 'w')
    #remove duplicates (because an instance saves per day of class)
    for j in courses:
        if j not in saved:
            saved.append(j)
    for j in saved:
        #remove nested list to get to the object
        for i in j:
            #formatting, saves it very specifically
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
            opened.write('\n')
    #close file, saves memory
    opened.close()
            
def save_homework():
    """
    

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
        # create course objects based on data read in
        course = Course((i[0], times, days))
        

if __name__ == "__main__":
    import doctest
    doctest.testmod()

