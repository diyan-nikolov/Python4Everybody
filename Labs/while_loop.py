# "While" loop lab

import random

print("Welcome to Guess The Number!")
print("The rules are simple. I will think of a number and you try to guess it.")

#generate a random number between 1 and 10
number = random.randint(1,10)

#keep track of whether the user has guessed your number
isGuessRight = False
counter = 0

while isGuessRight != True:
  guess = input("Guess a number between 1 and 10 (you are allowed 3 guesses): ")
  counter +=1
  if int(guess) == number:
    print("You guessed {}. That is right! You win!".format(guess))
    isGuessRight = True
  elif counter == 3:
      print("You are out luck. You do not have any more guesses")
      break
  else:
    print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))