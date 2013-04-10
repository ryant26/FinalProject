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
    
def save():
    """
    Saves all objects that exist as instances of a Course
    object. Called whenever you wish to save.
    """

    #retrieve all instances of courses to save
    courses = Course.get_all_instances()
    saved = []
    opened = open("save.txt", 'w')
    #remove duplicates (because an instance saves per day of course)
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

