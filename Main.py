import message
import process
import sched, time
from classHelper import Section

"""Setup function to be called when data.txt is empty, or manually for initial setup"""
def setup():
	switch = True
	sectionArray = []
	while switch:

		"""Prompts via terminal for class name, as well as URL, or 'end' to complete setup."""
		className = input("Which class would you like to receive updates for? Or, type 'end' to complete setup. > ")
		if className == 'end':
			switch = False
		else:
			process.resetData()
			classURL = input("Please provide the respective class' URL. > ")
			sectionArray.append(Section(className, classURL))

	"""Checks if sectionArray is empty (ie, no new sections added). If it has values, we initialize the Section in data.txt"""
	if sectionArray != []:
		process.initializeSection(sectionArray)


"""Loop to occur when the program is run, which checks for Section updates every 24 hours"""
def loop():
	sectionArray = process.recoverSections()
	while True:
		for section in sectionArray:
			message.buildAndSend(section)
		time.sleep(86400)

"""To be run whenever Main.py is called. Checks if data.txt is empty, if so, we setup, then we loop to check for updates"""
if process.isEmpty():
	setup()
loop()




"""https://classes.berkeley.edu/content/2019-spring-compsci-61b-001-lec-001"""