import random
myList = ["elephant", "carrot", "laptop", "zebra", "kangaroo", "mouse", "notebook"]
random.choice(myList)

def tries(10):
	while tries == 10:
..
		tries = tries - 1

def lets_play(letter):
	raw_input('Type a letter: {}') .format(letter)
	if letter in myList:
		return letter
		raw_input("That's right")
		return lets_play
	else:
		return 'Sorry that was wrong, try again!'
		return lets_play
