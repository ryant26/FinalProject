import random
import Interface

class Course:
    """
    Will initialize a class using the following format for info:
    info = ( "course name", ["start time", "end time"], [days])

    >>> course = Course(("ECE 212", [8, 9], ["Monday", "Wednesday", "Friday"]))
    >>> course.name == "ECE 212"
    True
    >>> print(Course._instances)
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

    def __init__(self, info):
        self.name = info[0]
        times = info[1]
        self.start = times[0]
        self.end = times[1]
        self.days = info[2]

        # insert into collection of instances
        
        for i in self.days:
            if i in Course._instances:
                Course._instances[i].append(self)
            else:
                Course._instances[i] = [self]

        r = str(hex(random.randint(0,16)))
        g = str(hex(random.randint(0,16)))
        b = str(hex(random.randint(0,16)))
        self._color = '#'+r+g+b
        for i in self.days:
            Interface.markBusy(self.name, self.start, self.end, i, 'blue')

    def get_start_time(self):
        return self.start
    
    def get_end_time(self):
        return self.end

    def get_all_instances(self):
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
    
    def save(self):
        """
        Saves a course object by it's data into a text file.
        Used to restore data from previous session on startup

 	>>> course = Course(("ECE 212", ["8:00", "9:00"], ["Monday", "Wednesday", "Friday"]))
    	>>> course.save()
        """
        opened = open("save.txt", 'w')
        st_start = str(self.start)
        st_end = str(self.end)

        opened.write(self.name)
        opened.write(st_start)
        opened.write(st_end)
        for i in self.days:
            opened.write(i)
        opened.write('/n')
        opened.close()
            


#def load():
    """
    Loads from a text file as many previously used
    instances of a course as are contained in the text file.
    This is done on startup to recreate the environment
    from previous shutdown. Will need to be iterated over
    in order to recreate all courses
    
    >>> course = Course(("ECE 212", ["8:00", "9:00"], ["Monday", "Wednesday", "Friday"]))
    >>> course.save
    >>> for x in load(): print(x)
    ("ECE 212", ["8:00", "9:00"], ["Monday", "Wednesday", "Friday"])
    
    """
    opened = open("save.txt", 'r')
    all_courses = opened.readlines()
    for i in all_courses:
        pass
        
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
