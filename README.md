FinalProject: Scheduling Program
================================

This is the scheduleing program created by:
-Brittany Lamorie
-Cody Otto 
-Ryan Thornhill

Usage:
======

Adding an Appointment:
----------------------

Adding an appointment can be done in one of two ways:
1.) Clicking on the "New Appointment Button"
2.) Clicking directly on the frame where you'd like an appointment to be added

Once you initiate one of the previous appointment adding sequences you will be greated with the appointment editing window
In here you can specify: 
-a name using the entry box 
-a start and end time with the drop boxes
-the days this appointment should be added to with the check boxes

Example:
If you wanted to add a chemistry class that ran Monday, Wednesday, Friday from 8 - 10:30 you would:
-Type the class name into the entry box (In this case chemistry )
-check the boxes labeled Monday, Wednesday and Friday 
-Change the start time to 8:00 and the end time to 10:30 
-Press the save button 

Once you press the save button, the appointment will be added to the scheduler AS WELL as the save.txt file. If at any time
you want to clear the current appointment editor window you can press the clear button. 

Once you hit save you'll notice the appointment has been added to the main schedule window.

It is important to note that you can still alter the start and end time of the appointment you are trying to add, if you open 
the appointment editor window by clicking on an empty frame. But this is the most convenient way to add hour long appointments
to the schedule. 

If you try to add an appointment that conflicts in any way with another appointment, it will not be saved. However, you will not
recieve an error message either. 


Deleting an Appointment:
------------------------

Deleting an appointment can be carried out in 2 ways:
1.) Selecting "New Appointment" Typing in the name of the appointment you want to delete
then press the delete button

2.) Double clicking on any filled in block of the appointment you want to delete to bring up
the appointment editor window and then press the delete button 

Both of these methods will delete an entire appointment off of the schedule, even if it spans multiple days/hours. Both of these methods
also delete the appointment out of the save.txt file. These methods are also used for deleting an "assignment" off of the schedule. 

Special Case Note**
When clicking on a block that has 2 half hour segments from different appointments it is important to notice WHICH name appears in the 
entry box when the appointment editor window is opened. That is the appointment that will be deleted when you press the delete button. If you delete 
one of these two appointments, close the editor window, click on the block the now contains only ONE half hour block you will now notice that the editor window
contains the name of that appointment, and it can now be de deleted in this fasion. 

Adding an Assignment:
---------------------
An assignment can be added by pressing the "Add Assignment" button to bring up the assignment editor window.
You can then enter:
-the name of the assignment into the entry box. 
-Select the day that it is due with the check boxes.
-Then choose the estimated completion time with the drop box.

While an assignment can be added at any point in time, it is most effective when you input your week schedule first.
The program will use load balancing to select the best time for you to work on the assignment. 
Deletion of an assignment works the same way as deletion of an appointment.  

Other Notes:
============

When an appointment or assignment is added to the scheduler it is also added to the save.txt. This means you can then close the program,
then re-open it and retain your current schedule information. One can also edit the save.txt them selfs. If you'd like to delete your entire schedule
and start from scratch, simply clear the contents of save.txt. 
