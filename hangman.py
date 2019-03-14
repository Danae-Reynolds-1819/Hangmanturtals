import random
import turtle
import tkinter


#opens the screen
window = turtle.Screen()
window.bgcolor("Dim Gray")

 #creates the hangman board and in correct letter box and explains the game
hang = turtle.Turtle()
hang.color("Medium Turquoise")
hang.pensize(6)
hang.shape("classic")
box = turtle.Turtle()
box.color("Medium Turquoise")
box.pensize(6)
box.shape("classic")


#turtle info for board
def hangBoard():
    hang.hideturtle()
    hang.penup()
    hang.back(100)
    hang.pendown()
    hang.back(200)
    hang.forward(100)
    hang.left(90)
    hang.forward(250)
    hang.right(90)
    hang.forward(100)
    hang.right(90)
    hang.forward(30)
box.hideturtle()
#makes the wrong letter box
def boxMake():
 box.penup()
 box.left(90)
 box.forward(200)
 box.right(90)
 box.pendown()
 for thing in range(2):
     box.forward(200)
     box.right(90)
     box.forward(100)
     box.right(90)
 getRandomWord(words)
#code for body
def head():
<<<<<<< HEAD
    hang.right(90)
    hang.circle(30)
    hang.penup()
    hang.left(90)
    hang.forward(60)




#if all strikes used then you lose


#if user wins, backgroud changes and goes to restart code


=======
   hang.right(90)
   hang.circle(30)
   hang.penup()
   hang.left(90)
   hang.forward(60)
def body():
   hang.pendown()
   hang.forward(80)
   hang.back(70)
def leftarm():
   hang.left(45)
   hang.forward(50)
   hang.back(50)
def rightarm():
   hang.right(90)
   hang.forward(50)
   hang.back(50)
def leftleg():
   hang.left(45)
   hang.forward(70)
   hang.left(45)
   hang.forward(50)
   hang.back(50)
def rightleg():
   hang.right(90)
   hang.forward(50)
   hang.back(50)


words = 'ant salmon zebra'.split()

def getRandomWord(wordList):
    # This function returns a random string from the passed list of strings.
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print([len(missedLetters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

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


print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

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
                break
        if foundAllLetters:
            print('Yes! The secret word is "' + secretWord + '"! You have won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        # Check if player has guessed too many times and lost
        if len(missedLetters) == len(secretWord) - 1:
            head()
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
        if len(missedLetters)==len(secretWord)-1:
            body()
        if len(missedLetters)==len(secretWord)-1:
            leftarm()
        if len(missedLetters)==len(secretWord)-1:
            rightarm()
        if len(missedLetters)==len(secretWord)-1:
            leftleg()
        if len(missedLetters)==len(secretWord)-1:
            rightleg()
            gameIsDone = True



    # Ask the player if they want to play again (but only if the game is done).
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break
>>>>>>> c48f3fa3b7270ab3a61013d8027d5fd169fca810
hangBoard()
boxMake()

tkinter.mainloop()
