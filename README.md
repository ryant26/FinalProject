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
	
Brittany can also change her spin boxes to send numbers to cody instead of strings. Might be the easiest approach...
Still need:
	-Need to call Brittany's code when clicking a frame
			Possible Design Idea:
			-If she makes her code into a class then each schedule frame can have its own instance of
			the "appointment editor" and the options will be saved for that particular appointment


	-Need code for dragging and dropping, I can write the interface side. Me and Cody will need to colab on how
	to handle that properly
