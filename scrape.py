import requests
from bs4 import BeautifulSoup
from ast import literal_eval
from json import dumps

url = 'https://classes.berkeley.edu/content/2019-spring-compsci-61a-001-lec-001'
response = requests.get(url)
html = response.content
className = "CS61A"

def processHTML():
	returnDict = {}

	soup = BeautifulSoup(html, 'lxml')

	divAttributes = soup.find("div", {'class' : 'handlebarData'}).attrs

	enrollmentData = divAttributes.get('data-enrollment')

	enrollmentDict = literal_eval(enrollmentData).get('available').get('enrollmentStatus')

	openEnrollment = enrollmentDict.get('status').get('description')

	infoCalls = ["enrolledCount", "reservedCount", "waitlistedCount", "maxEnroll", "maxWaitlist"]

	returnDict['status'] = openEnrollment

	for call in infoCalls:
		returnDict[call] = enrollmentDict.get(call)

	return returnDict


def exportDictionary(dictionary):
	with open('data.txt', 'w') as file:
		file.write(dumps(dictionary))

