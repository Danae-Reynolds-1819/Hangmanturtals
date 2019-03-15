#Imports Libraries
import random
import turtle
import tkinter
import time

#opens the screen
window = turtle.Screen()
window.bgcolor("Dim Gray")

 #creates the hangman board and gives the color pen size
hang = turtle.Turtle()
hang.color("Medium Turquoise")
hang.pensize(6)
hang.shape("classic")

#This is the SECOND turtle for drawing the body
hangs = turtle.Turtle()
hangs.color("Medium Turquoise")
hangs.pensize(6)
hangs.shape("classic")


#turtle info for making the hangboard
def hangBoard():
    hang.speed(0)
    hang.hideturtle()
    hang.back(200)
    hang.forward(100)
    hang.left(90)
    hang.forward(250)
    hang.right(90)
    hang.forward(100)
    hang.right(90)
    hang.forward(30)
    hangs.hideturtle()
    hangs.penup()
    hangs.left(90)
    hangs.forward(220)
    hangs.left(180)
    hangs.pendown()
hangBoard()
#Uses code to make the body after each incorrect guess
def man():
#This makes the head
   hangs.speed(7)
   hangs.right(90)
   hangs.circle(30)
   hangs.penup()
   hangs.left(90)
   hangs.forward(60)
   time.sleep(2)
def manbody():
#Makes the body
   hangs.pendown()
   hangs.forward(80)
   hangs.back(70)
   time.sleep(2)
def manleftarm():
#Makes the left arm
   hangs.left(45)
   hangs.forward(50)
   hangs.back(50)
def manrightarm():
#Makes right arm
   hangs.right(90)
   hangs.forward(50)
   hangs.back(50)
def manleftleg():
#Makes left leg
   hangs.left(45)
   hangs.forward(70)
   hangs.left(45)
   hangs.forward(50)
   hangs.back(50)
def manrightleg():
#Makes right leg
   hangs.right(90)
   hangs.forward(50)
   hangs.back(50)

#This is the word list
words = 'jazz jazzy yewhaw dab wierd accommodate cemetery caribbean Arctic xylophone daiquiri'.split() #Split strings the words into a list

def getRandomWord(wordList):
# This function returns a random string from the passed list of strings.
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

#This code sets up the missed letter count
def displayBoard(missedLetters, correctLetters, secretWord):
    print([len(missedLetters)])
    print()
    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()
#Sets up the blanks
    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): # replace blanks with correctly guessed letters
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: # show the secret word with spaces in between each letter
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    # Returns the letter the player entered. This function makes sure the player entered a single letter, and not something else.
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess

def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

#Resets missed letters and the correct letters as well as the random word
print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

#Ture keeps the game runing
while True:
    displayBoard(missedLetters, correctLetters, secretWord)

    # Let the player type in a letter.
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Check if the player has won
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break #Stops first loop
        #Once all letters, it reveals the secert word and tell player they won. Then it takes them to 'gameIsDone.'
        if foundAllLetters:
            print('Yes! The secret word is "' + secretWord + '"! You have won!')
            gameIsDone = True
    # If guessed incorrectly it directs them to 'missedLetters'
    else:
        missedLetters = missedLetters + guess

        #If one miss occures, a body part will be drawn. Once all 6 body parts are done, game is done
        if len(missedLetters) == 7:
            displayBoard(missedLetters, correctLetters, secretWord)
        if len(missedLetters)==2-1:
            man()
        if len(missedLetters)==3-1:
            manbody()
        if len(missedLetters)==4-1:
            manleftarm()
        if len(missedLetters)==5-1:
            manrightarm()
        if len(missedLetters)==6-1:
            manleftleg()
        if len(missedLetters)==7-1:
            manrightleg()
            # Check if player has guessed too many times and lost
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')

            gameIsDone = True




    # Ask the player if they want to play again (but only if the game is done).
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break #This break ends the game completely
#Keeps turtle window open
tkinter.mainloop()

