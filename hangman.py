import random
  

def is_valid_input(letter, letters_guessed):
    if len(letter) != 1:
        print '\nCan only be one letter'
        return False

    if letter.lower() not in 'abcdefghijklmnopqrstuvwxyz':
        print '\nMust be a letter'
        return False

    if letter in letters_guessed:
        print '\nAlready guessed'
        return False
    return True

fin = open("words.txt").read().splitlines()
word = random.choice(fin)

tries = 10
letters_guessed = ''
wrong_letters = ''

while tries > 0:
    wrong = 0

    for i in word:
        if i in letters_guessed:
            print i,
        else: 
            print '_',
            wrong = wrong + 1

    if wrong == 0:
        print "\nYou won!"
        break
    print

    letter = raw_input('Type a letter: ') 

    if is_valid_input(letter, letters_guessed):
        letters_guessed = letters_guessed + letter                     

    if letter not in word and letter not in wrong_letters:
        tries = tries - 1
        wrong_letters = wrong_letters + letter
        print "Try again. You have", + tries, 'more tries.'

    if tries == 0:
        print 'You lose'
        print 'The word was: ' + word

    print "\nLetters Guessed: " + letters_guessed
