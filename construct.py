import scrape
import process
import message
from scrape import className
from json import dumps
from ast import literal_eval

messageHelpers = dict({"status" : "Enrollment Status", "enrolledCount" : "Enrollment Count", "reservedCount" : "Reserved Spots Count", "waitlistedCount" : "Waitlist Count", "maxEnroll" : "Class Size", "maxWaitlist" : "Waitlist Size"})

def createMessage():
	msg = scrape.className
	msg = msg + ": "
	changes = process.readAndCompare()
	if changes != None:
		for key in changes:
			msg = msg + messageHelpers[key] + " has been updated to " + str(changes[key]) + ". "

	print(msg)
