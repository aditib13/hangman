import random


# WHAT NEVER TO DO

# while len(letter) >= 1:
#     if len(letter) > 1:
#         print('Please enter one letter.')
#     return game()
#     if letter in letters_guessed:
#         print('You have already guessed that letter. Try again.')
#     return game()
#     if letter not in 'abcdefghijklmnopqrstuvwxyz':
#         print('Please enter a letter.')
#     return game()
#     if len(letter) == 1:
#         continue


# ONLY DO THIS IF YOU DON'T KNOW WHAT YOU'RE DOING AND TOO LAZY TO BOTHER TO FIGURE IT OUT
# if len(letter) > 1:
#     while True:
#             print("Error! Please only enter 1 letter at a time")
#             try_again = raw_input('Try again: ')
#             if len(try_again) == 1:
#                 break
#             else:
#                 continue


# THIS IS WHY YOU SHOULDN'T DO DRUGS
# if len(letter) != 1:
#     while True:
#         print("Error! Please only enter 1 letter at a time")
#         return game()
# # else:
# #     letter in letters_guessed: 
# #         letters_guessed.remove(letter)
#         letter = raw_input('Type a letter: ')  
#         if letter == 0:
#             continue   
#         else:
#             break   

def is_valid_input(letter, letters_guessed):
    """Checks if input is valid"""
    if len(letter) != 1:
        print 'Can only be one letter'
        return False

    print 23234234234234
    if letter.lower() not in 'abcdefghijklmnopqrstuvwxyz':
        print 'Must be a letter'
        return False

    if letter in letters_guessed:
        print 'Already guessed'
        return False
    return True

fin = open("words.txt").read().splitlines()
word = random.choice(fin)

tries = 10
letters_guessed = ''


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

    if letter not in word:
        tries = tries - 1
        print "\nTry again. You have", + tries, 'more tries.'

    if tries == 0:
        print 'You lose'
        print 'The word was: ' + word





    print "\nLetters Guessed: " + letters_guessed



