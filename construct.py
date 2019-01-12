import process

from classHelper import Section
from json import dumps
from ast import literal_eval

"""Dictionary relating HTML tags to english words to be used in message construction"""
messageHelpers = dict({"status" : "Enrollment Status", "enrolledCount" : "Enrollment Count", "reservedCount" : "Reserved Spots Count", "waitlistedCount" : "Waitlist Count", "maxEnroll" : "Class Size", "maxWaitlist" : "Waitlist Size"})

"""Creates a message based on a specific section through calls to process, constructs a string to best
express the data being sent to the user"""
def createMessage(section):
	msg = ''
	changes = process.readAndCompare(section)
	if changes != None:
		msg = section.name + ": "
		for key in changes:
			msg = msg + messageHelpers[key] + " has been updated to " + str(changes[key]) + ". "


	return(msg)


""" commenting out for testing
print(createMessage(Section('CS61A', 'https://classes.berkeley.edu/content/2019-spring-compsci-61a-001-lec-001'))) """