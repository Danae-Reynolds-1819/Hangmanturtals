#imports libraries
import turtle
import tkinter
import random

#opens the screen
window = turtle.Screen()
window.bgcolor("Dim Gray")

#list for words
wrong = ''
words = 'jazz jazzy yeehaw dab'.split()


#creates the hangman board and in correct letter box
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
 boxMake()

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
  wordlist=''
  getRandomWord(wordlist)

#user picks a word
def getRandomWord(wordlist):
    wordIndex = random.randint(0, len(wordlist)-1)
    return wordlist[wordIndex]

#daches are created
secrectWord = getRandomWord(words)
blanks = '_'* len(secrectWord)
#user type in one letter for word
def letter(secrectWord):
  letter=input("Please guess a letter: ")
  for i in range(len(secrectWord)):#if correct figuers where letter goes and puts it there
      if secretWord[i] in correctLetters:
          blanks = blanks[:i]+secretWord[i]+blanks[i+1]
  for letter in blanks:
      print(letter, end='')
  print()


def again():
    letter(secrectWord)



#if wrong the letter will go to a box and makes a part of the body
def makeBoi():
  for thing in range(6-1):
      if thing==6:
          head()
      else:
          print("bye")
def head():
    hang.right(90)
    hang.circle(30)
    hang.penup()
    hang.left(90)
    hang.forward(60)




#if all strikes used then you lose


#if user wins, backgroud changes and goes to restart code


hangBoard()
tkinter.mainloop()


