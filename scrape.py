import requests
from bs4 import BeautifulSoup
from ast import literal_eval
from json import dumps
"""
url = 'https://classes.berkeley.edu/content/2019-spring-compsci-61a-001-lec-001'
response = requests.get(url)
html = response.content
className = "CS61A" """


"""Scrapes information from relevant section URL, which is a Section instance variable """
def processHTML(section):
	""" Initializes relevant information from passed in classHelper class """
	url = section.url
	response = requests.get(url)
	html = response.content
	className = section.name

	""" Initializes dictionary to store updated values, processes HTML and fills dict """
	returnDict = {}

	soup = BeautifulSoup(html, 'lxml')

	"""Using BeautifulSoup to parse important data"""
	divAttributes = soup.find("div", {'class' : 'handlebarData'}).attrs
	enrollmentData = divAttributes.get('data-enrollment')
	enrollmentDict = literal_eval(enrollmentData).get('available').get('enrollmentStatus')
	
	"""Finds enrollment status (open or closed), located in a different part of the HTML so seperate method"""
	openEnrollment = enrollmentDict.get('status').get('description')

	"""Array holding HTML tags of data desired"""
	infoCalls = ["enrolledCount", "reservedCount", "waitlistedCount", "maxEnroll", "maxWaitlist"]	
	returnDict['status'] = openEnrollment
	
	"""Filling dictionary with necessary class information"""

	for call in infoCalls:
		returnDict[call] = enrollmentDict.get(call)

	return returnDict

	"""helper function, currently unused"""
def exportDictionary(dictionary):
	with open('data.txt', 'w') as file:
		file.write(dumps(dictionary))

