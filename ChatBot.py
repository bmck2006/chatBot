"""
CHATBOT v1.0
BY: Brian McKeown

This program runs a simple chatbot
"""
# (terminal path:) python "/Users/bmckeown2011/Desktop/Python Files/ChatBot.py"


from random import randrange
from time import sleep
from datetime import datetime

now = datetime.now()
nowStamp = '%s/%s/%s  %s:%s' % (now.month, now.day, now.year, now.hour, now.minute)
timeStamp = '%s:%s : ' % (now.hour, now.minute)

userGreetings = ['hola', 'hello', 'hi', 'hi', 'hey!','hey','yo', 'hola!', 'hello!', 'whats up', "what's up" ]
bot1greetingResponse = ['Yoo dude, wuddup!?', 'sup dude', "eyyy whats good?", 'yo yo yo whats good']
bot2greetingResponse = ['HIII, HOW ARE YOU!?', 'HIIII!!! <3 <3 <3, HOW ARE YOU!!', 'HIHIHIHIHI :)!!! HOW ARE YOU?']
bot3greetingResponse = ['...hi. sup', 'hi... sup']
bot4greetingResponse = ['HayYyy you, how you do?', 'Hiiiii, how fabulousss are you today :)', 'Hollaa girllll, how R you??']
bot5greetingResponse = ['Hi! like omg how are you?', 'Heyy, omgosh! whats up??', 'HeyYyY LOLz how are you?']

bot1greeting = bot1greetingResponse[randrange(0,len(bot1greetingResponse))]
bot2greeting = bot2greetingResponse[randrange(0,len(bot2greetingResponse))]
bot3greeting = bot3greetingResponse[randrange(0,len(bot3greetingResponse))]
bot4greeting = bot4greetingResponse[randrange(0,len(bot4greetingResponse))]
bot5greeting = bot5greetingResponse[randrange(0,len(bot5greetingResponse))]

question = ['good u?','good you?','good, you?','good, u?','good, you?','good, you?','not much','not much u?','not much u']
responses = ['nothin much',"not much"]
random_response = responses[randrange(0, len(responses))]
goodbye = ['bye']
signoff_response = ["SIGNED OFF: "]

def user1loop():
	while True:
		userInput = raw_input(">>> ")
		userInput = str(userInput.lower())
		if userInput in userGreetings:
			sleep(1)
			print(bud1 + ": " + bot1greeting)
		elif userInput in question:
			sleep(1)
			print(bud1 + ": " + random_response)
		elif userInput in goodbye:
			sleep(1)
			print(bud1 + ": " + signoff_response[0] + timeStamp)
		else:
			sleep(1)
			print(bud1 + ": " + "g2g dude, later!")
def user2loop():
	while True:
		userInput = raw_input(">>> ")
		userInput = str(userInput.lower())
		if userInput in userGreetings:
			sleep(1)
			print(timeStamp + bot2greeting)
		elif userInput in question:
			sleep(1)
			print(timeStamp + random_response)
		else:
			sleep(1)
			print(timeStamp + "I did not understand what you said")
def user3loop():
	while True:
		userInput = raw_input(">>> ")
		userInput = str(userInput.lower())
		if userInput in userGreetings:
			sleep(1)
			print(timeStamp + bot3greeting)
		elif userInput in question:
			sleep(1)
			print(timeStamp + random_response)
		else:
			sleep(1)
			print(timeStamp + "I did not understand what you said")
def user4loop():
	while True:
		userInput = raw_input(">>> ")
		userInput = str(userInput.lower())
		if userInput in userGreetings:
			sleep(1)
			print(timeStamp + bot4greeting)
		elif userInput in question:
			sleep(1)
			print(timeStamp + random_response)
		else:
			sleep(1)
			print(timeStamp + "I did not understand what you said")
def user5loop():
	while True:
		userInput = raw_input(">>> ")
		userInput = str(userInput.lower())
		if userInput in userGreetings:
			sleep(1)
			print(timeStamp + bot5greeting)
		elif userInput in question:
			sleep(1)
			print(timeStamp + random_response)
		else:
			sleep(1)
			print(timeStamp + "I did not understand what you said")


#program run:
print "*********************\nWelcome to MESSENGER SIM 1.0\n *********************\n"
sleep(1)

user_name = str(raw_input("Let's get started!\nWhat is your name?\n>>>"))
user_name = user_name.upper()

print "Hello " + user_name + "!\n"
sleep(1)
print "\nPlease choose a buddy to chat with!"
print "Choose from your available buddies on your BUDDY LIST below!\n"
sleep(2)
print "\nSIGNING IN..."
sleep(3)

print "\n****************************************\n" + user_name + "'S BUDDY LIST\n****************************************"
print "AVAILABLE"
print "\t1) sk8rGuy_99\n\t2) PSYchOxSARAx\n\t3) EMOpunkPete\n\t4) SassyStevey\n\t5) CheerQueenKate77"
print"OFFLINE"
print "\tJoeJeepz\n\tMollzDollz123\n\tyoMama2016"
print"****************************************"
sleep(1)

bud1 = "sk8rGuy_99"
bud2 = "PSYchOxSARAx"
bud3 = "EMOpunkPete"
bud4 = "SassyStevey"
bud5 = "CheerQueenKate77"
print "Enter the number of the buddy you wish to Instant Message!"
buddy_selection = int(raw_input(">>> "))
sleep(1)
print "\n****************************************"

if buddy_selection == 1:
	print "New IM Window: " + bud1 + ": " + nowStamp
	user1loop()
elif buddy_selection == 2:
	print "New IM Window: " + bud2 + ": " + nowStamp
	user2loop()
elif buddy_selection == 3:
	print "New IM Window: " + bud3 + ": " + nowStamp
	user3loop()
elif buddy_selection == 4:
	print "New IM Window: " + bud4 + ": " + nowStamp
	user4loop()
elif buddy_selection == 5:
	print "New IM Window: " + bud5 + ": " + nowStamp
	user5loop()
else:
	print "Incorrect selection! Please try again!"
	selectBuddy()



