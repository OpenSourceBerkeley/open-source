import nexmo
from construct import createMessage

"""personal client information"""
client = nexmo.Client(key='KEY_HERE', secret='SECRET_HERE')

"""Checks if the passed in message is empty or None, prints a copy of the message being sent, 
	prints information regarding the Nexmo transaction ocurring, and sends the message"""
def sendMessage(msg):
	if msg == '' or msg == None:
		print("No updates. Empty message will not be sent")
		return
	print("Sending message: " + msg)
	print(client.send_message({'from':'NUM_FROM', 'to':'NUM_TO', 'text': msg}))


"""Makes call to construct.createMessage by passing in section, exports returned message to sendMessage"""
def buildAndSend(section):
	sendMessage(createMessage(section))
