import nexmo
from construct import createMessage

"""personal client information"""
client = nexmo.Client(key='3057bdb4', secret='uG4jgD0ob23tGHi7')

"""Checks if the passed in message is empty or None, prints a copy of the message being sent, 
	prints information regarding the Nexmo transaction ocurring, and sends the message"""
def sendMessage(msg):
	if msg == '' or msg == None:
		print("No updates. Empty message will not be sent")
		return
	print("Sending message: " + msg)
	print(client.send_message({'from':'12035338039', 'to':'16192406117', 'text': msg}))


"""Makes call to construct.createMessage by passing in section, exports returned message to sendMessage"""
def buildAndSend(section):
	sendMessage(createMessage(section))
