#import numpy

class Course:
    """
    Will initialize a class using the following format for info:
    info = ( "course name", ["start time", "end time"], [days])

    >>> course = Course(("ECE 212", ['8:00', '9:00'], ["Monday", "Wednesday", "Friday"]))
    >>> course.name == "ECE 212"
    True
    >>> course.start
    '8:00'
    >>> course.end
    '9:00'
    >>> course.days
    ['Monday', 'Wednesday', 'Friday']
    >>> course.each_day()
    [('Monday', '8:00', '9:00'), ('Wednesday', '8:00', '9:00'), ('Friday', '8:00', '9:00')]
    """
    def __init__(self, info):
        self.name = info[0]
        times = info[1]
        self.start = times[0]
        self.end = times[1]
        self.days = info[2]

    def change_time(self, start, end):
        """
        Change the time to a new (start,end) pair
        >>> course = Course(("ECE 212", ["8:00", "9:00"], ["Monday", "Wednesday", "Friday"]))
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
    
   # def save(self):
        """
        Saves a course object by it's data into a text file.
        Used to restore data from previous session on startup
        NOTE
        Must have numpy module installed
        """
       # numpy.savetxt(save.txt, course.name)
       # numpy.savetxt(save.txt, [course.start, course.end])
       # numpy.savetxt(save.txt, course.days, newline = '\n')

#def load():
    """
    Loads from a text file as many previously used
    instances of a course as are contained in the text file.
    This is done on startup to recreate the environment
    from previous shutdown. Will need to be iterated over
    in order to recreate all courses
    NOTE
    Must have numpy module installed
    
    >>> course = Course(("ECE 212", ["8:00", "9:00"], ["Monday", "Wednesday", "Friday"]))
    >>> course.save
    >>> for x in load(): print(x)
    ("ECE 212", ["8:00", "9:00"], ["Monday", "Wednesday", "Friday"])
    
    """
   # info = numpy.loadtxt(save.txt)
   # yield Course(info) 
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
