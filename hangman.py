import random


myList = ["elephant", "carrot", "laptop", "zebra", "kangaroo", "mouse", "notebook"]

random.choice(myList)



def tries(10):
	while tries == 10:
# TODO
		tries = tries - 1

def play():
	letter = raw_input('Type a letter: ') 



	if letter in myList:
	
		print letter
		raw_input("That's right")
	
		play()
	else:
	
		print 'Sorry that was wrong, try again!'
	

		play()

