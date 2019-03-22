# Imports Libraries
import random
import turtle
import tkinter
import time

# opens the screen
window = turtle.Screen()
window.bgcolor("Dim Gray")

# creates the hangman board and gives the color pen size
hang = turtle.Turtle()
hang.color("Medium Turquoise")
hang.pensize(6)
hang.shape("classic")

# This is the SECOND turtle for drawing the body
hangs = turtle.Turtle()
hangs.color("Medium Turquoise")
hangs.pensize(6)
hangs.shape("classic")


# turtle info for making the hangboard
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
# Uses code to make the body after each incorrect guess


def man():
    # This makes the head
   hangs.speed(7)
   hangs.right(90)
   hangs.circle(30)
   hangs.penup()
   hangs.left(90)
   hangs.forward(60)
   time.sleep(2)


def manbody():
    # Makes the body
   hangs.pendown()
   hangs.forward(80)
   hangs.back(70)
   time.sleep(2)


def manleftarm():
    # Makes the left arm
   hangs.left(45)
   hangs.forward(50)
   hangs.back(50)


def manrightarm():
    # Makes right arm
   hangs.right(90)
   hangs.forward(50)
   hangs.back(50)


def manleftleg():
    # Makes left leg
   hangs.left(45)
   hangs.forward(70)
   hangs.left(45)
   hangs.forward(50)
   hangs.back(50)


def manrightleg():
    # Makes right leg
   hangs.right(90)
   hangs.forward(50)
   hangs.back(50)

# This is the word list:


words = 'jazz jazzy yewhaw dab wierd accommodate cemetery caribbean Arctic xylophone daiquiri watertemple zelda link kokiri'.split() #Split strings the words into a list


def getRandomWord(wordList):
    # This function returns a random string from the passed list of strings.
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

# This code sets up the missed letter count


def displayBoard(missedLetters, correctLetters, secretWord):
    print([len(missedLetters)])
    print()
    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()
# Sets up the blanks
    blanks = '_' * len(secretWord)  # counts the seceret word for the number of dashes

    for i in range(len(secretWord)):  # replace blanks with correctly guessed letters
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:  # show the secret word with spaces in between each letter
        print(letter, end=' ')  # leaves a space at the end
    print()

def getGuess(alreadyGuessed):
    # Returns the letter the player entered. This function makes sure the player entered a single letter, and not something else.
    while True:
        print('Guess a letter: ')  # Tells user to guess a letter
        guess = input()  # Takes user input
        guess = guess.lower()
        if len(guess) != 1:  # Tells that if the guess does not equal 1 letter, goes to the print and tells user to enter ONE letter
            print('Please enter a single letter.')  # If the user types in more than one letter, this instruction will show up.
        elif guess in alreadyGuessed:  # If their guess has alredy been guessed, the statement below will be asked
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':  # Makes sure that the guess is in the alphabet
            print('Please enter a LETTER.')  # If they guess a number, this statement will pop up
        else:
            return guess  # If the input has nothing wrong, It'll keep on asking for input.


def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    hangs.clear()
    hangs.penup()
    hangs.hideturtle()
    hangs.home()
    hangs.penup()
    hangs.left(90)
    hangs.forward(220)
    hangs.left(180)
    hangs.pendown()
    return input().lower().startswith('y')



# Resets missed letters and the correct letters as well as the random word
print('W E L C O M E T O H A N G M A N') # Welcome title
missedLetters = ''  # Sets missed letters to ZERO
correctLetters = ''  # Sets correct letter to  ZERO
secretWord = getRandomWord(words)  # makes 'seceretWord' equal the random word as well as choose the random word.
gameIsDone = False  # The game is no over, the loop is not over.

# True keeps the game running
while True:
    displayBoard(missedLetters, correctLetters, secretWord)  # On the input screen it sets it up accordingly

    # Let the player type in a letter.
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:  # If the guess is correct...
        correctLetters = correctLetters + guess

        # Check if the player has won
        foundAllLetters = True  # If they have found all the correct letters:
        for i in range(len(secretWord)):  # For the amount of numbers in the seceret word
            if secretWord[i] not in correctLetters:  # If the letters guessed are not in the correct word:
                foundAllLetters = False  # They did not find all the letters
                break  # Stops first loop
        # Once all letters, it reveals the secert word and tell player they won. Then it takes them to 'gameIsDone.'
        if foundAllLetters:  # If the guest found all the letters:
            print('Yes! The secret word is "' + secretWord + '"! You have won!') # Types what the word was as states you've won:)
            gameIsDone = True  # Stops the game. Its now complete
    # If guessed incorrectly it directs them to 'missedLetters'
    else:
        missedLetters = missedLetters + guess

        # If one miss occurs, a body part will be drawn. Once all 6 body parts are done, game is done
        if len(missedLetters) == 7:
            displayBoard(missedLetters, correctLetters, secretWord)
        if len(missedLetters) == 2-1: # This will go up tp the def to draw the head afer the first missed letter
            man()
        if len(missedLetters) == 3-1: # Goes to the def to make the body after the second missed letter
            manbody()
        if len(missedLetters) == 4-1: # Goes to the def to make the left arm after the third missed letter
            manleftarm()
        if len(missedLetters) == 5-1: # Goes to the def to make the right arm after the fourth missed letter
            manrightarm()
        if len(missedLetters) == 6-1: # Goes to the def to make the left leg afer the fifth missed letter
            manleftleg()
        if len(missedLetters) == 7-1: # Goes to the def to make the right leg and ends the game ofter the sixth missed letter
            manrightleg()
            # Check if player has guessed too many times and lost
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')

            gameIsDone = True

    # Ask the player if they want to play again (but only if the game is done).
    if gameIsDone:
        if playAgain():
            missedLetters = ''  # Sets missed letters to ZERO
            correctLetters = ''  # Sets correct letters to ZERO
            gameIsDone = False
            secretWord = getRandomWord(words) # Picks a RandomWord
        else:
            break  # This break ends the game completely
# Keeps turtle window open
tkinter.mainloop()
