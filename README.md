This is the solution for ProtonMail Junior QA Engineer task.
In this task i was expected to:

	● Select a test automation framework. Please refrain from using keyword-driven, record &
	playback tools
	● Research and use good practices on organising and designing automated tests (e.g.
	PageObject model)
	● Write a set of automated tests for the following scenarios:
	1. Create a label/folder
	2. Modify a label/folder
	3. Delete a label/folder
	4. Change order of labels/folders in the list
	● Document the project with a readme file.

For this solution i chose Selenium test automation framework with Chrome web browser driver.
The tests were writen using Python programing language. When i was writing automation tests 
I used POM practices to make the page objects reusable in other scripts. I also wrote a login case
as setUp for the test in order for the to be fully functional. Python console prints the test result,
I havent implemented any reporting librarys in this assignment.
