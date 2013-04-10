FinalProject
============

March 30:
Playing around trying to create menues in TK 

April 5:
All schedule boxes are now hoverable, I made each frame it's own class 
Everything is fully resizeable, might need to adjust minsizes once appointments are in there

April 6:
Double clicking any frame within the schedule or clicking the "new appointment" button will open up another window.
This will be changed to a handler which calls Brittany's code.

There is no code yet for if there is something already within the frame to call Brittany's code differently.

April 8:
Added some methods to fill the frame when an appointment is added. Also, now splits frames in 2 when an appointment
starts or ends on the half. 

Curently working on the destroy method to make frames available once an appointment is changed or edited. Need to think
of elegant way to handle the splits. 

Trying to find a way to work with strings that cody passes, but that doesn't look like it's going to work. Instead I'm thinking 
cody should convert the times he gets into floats eg. 
	'8:30' = 8.5, '2:00' = 14, "2:30" = 14.5
	
April 9:
First working prototype is complete!!

Notes:
I fixed the bug where 2 half hour classes in the same block will cause an overwrite. 
