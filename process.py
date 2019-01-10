import scrape
from json import dumps
from ast import literal_eval



def readAndCompare():
	keys = ["status", "enrolledCount", "reservedCount", "waitlistedCount", "maxEnroll", "maxWaitlist"]
	
	changed = dict()
	
	oldInfo = literal_eval(open('data.txt', 'r').read())
	
	newInfo = scrape.processHTML()
	
	sameInfo = oldInfo == newInfo
	
	if sameInfo == False:
		for key in keys:
			if newInfo.get(key) != oldInfo.get(key):
				changed[key] = newInfo.get(key)


		open('data.txt', 'w').close()

		with open('data.txt', 'w') as file:
			file.write(dumps(newInfo))
	

	return changed