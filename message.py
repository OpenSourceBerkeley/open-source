import nexmo
import construct

client = nexmo.Client(key='3057bdb4', secret='uG4jgD0ob23tGHi7')

def sendMessage(msg) :
	if msg == '':
		print("Empty message will not be sent")
		return
	print(client.send_message({'from':'12035338039', 'to':'16192406117', 'text': msg}))

sendMessage(construct.createMessage())