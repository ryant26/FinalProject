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

Still need:
	-Need to call Brittany's code when clicking a frame
			Possible Design Idea:
			-If she makes her code into a class then each schedule frame can have its own instance of
			the "appointment editor" and the options will be saved for that particular appointment

	-Now that I have decided to make each frame a class I was thinking that each frame could "extend"
	Cody's Class; then each frame will be acting as an appointment itself. Might make things easier for editing?
	Will probably enable the dragging and dropping of appointments feature. 

	-Need code for dragging and dropping, I can write the interface side. Me and Cody will need to colab on how
	to handle that properly