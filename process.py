import scrape
import os
from classHelper import Section
from json import dumps
from ast import literal_eval

"""Class dedicated to processing information in data.txt, makes comparisons with calls to scrape.py
	K. M. Tucker """

"""Checks if data.txt is empty"""
def isEmpty():
	return os.stat('data.txt').st_size == 0



"""Clears data.txt, used primarily in setup"""
def resetData():
	reset = open('data.txt', 'w')
	reset.close()


"""Initializes section information in data.txt, takes an array of Section objects"""
def initializeSection(sectionArray):
	fileInfo = []
	for section in sectionArray:
		fileInfo.append(section.name)
		fileInfo.append(section.url)
		fileInfo.append(scrape.processHTML(section))

	output = open('data.txt', 'w')
	for line in fileInfo:
		output.write(str(line))
		output.write("\n")
	output.close()


"""Recovers sections from data.txt, creates new Section objects with name and URL, exports in Array"""
def recoverSections():
	data = [line.rstrip('\n') for line in open('data.txt', 'r')]
	sectionNames = []
	sectionURLs = []
	sectionArray = []

	for x in range(len(data)):
		if x % 3 == 0:
			sectionNames.append(data[x])
		if (x + 2) % 3 == 0:
			sectionURLs.append(data[x])

	for x in range(len(sectionNames)):
			currSec = Section(sectionNames[x], sectionURLs[x])
			sectionArray.append(currSec)

	return sectionArray

	

"""Processes the scraped data from scrape.py per individual Section, compares it to saved data in data.txt
	Updates data if changes are detected"""
def readAndCompare(section):
	"""Keys of HTML objects which we will be calling"""
	keys = ["status", "enrolledCount", "reservedCount", "waitlistedCount", "maxEnroll", "maxWaitlist"]
	index = 0
	changed = None
	"""String of old info to be pulled from data.txt"""
	oldInfo = ''

	""" Puts data.txt into an array of string objects (index = line number) """
	data = [line.rstrip('\n') for line in open('data.txt', 'r')]

	"""Finds the proper index of specific Section object, saves its data (located two rows below the name)"""
	for x in range(len(data)):
		if data[x] == section.name:
			oldInfo = data[x + 2]
			index = x + 2

	"""Scrapes new data from the URL, evaluates the string pulled from data.txt into a dictionary (oldInfo) """
	newInfo = scrape.processHTML(section)
	oldInfo = literal_eval(oldInfo)
	
	"""Comparator for information"""
	sameInfo = oldInfo == newInfo
	
	"""Detects where discrepencies exist between old and new data, adds it to 'changed' dictionary of HTML attributes and values"""
	if sameInfo == False:
		changed = dict()
		for key in keys:
			if newInfo.get(key) != oldInfo.get(key):
				changed[key] = newInfo.get(key)

		"""Takes new info, converts from dictionary to string, rewrites data array where old values have been updated"""
		data[index] = dumps(newInfo)

		"""Rewrites array of Strings (data array) to data.txt, only updates necessary lines"""
		output = open('data.txt', 'w')
		for line in data:
			output.write(line)
			output.write("\n")
		output.close()
	
	"""Returns dictionary of updated values"""
	return changed
