#Corinne Haley
#Practice Script
#Rock/Paper/Scissors Game

#must import random so computer and choose from list.
import random

print("\n")
#ask for the player to choose their weapon with string and input.
while True:
myInput = input("Enter a choice (rock, paper, scissors): ")
print("\n")

#list of weapons
weapons = ["rock", "paper", "scissors"]

#use random.choice (module.method) to have computer choose a weapon
compChoice = random.choice(weapons)

#line 17 uses a formatted string literal indicated by the "f" and the curly braces.
print(f"You chose {myInput}, and the computer chose {compChoice}.")

#run if/elif/else statements to compare the compchoice to myInput
if myInput == compChoice:
    print(f"You both chose {myInput}.  It's a tie!")
elif myInput == "rock":
    if compChoice == "scissors":
        print("Rock smashes scissors!  You win!")
elif myInput == "rock":
    if compChoice == "paper":
        print("Paper covers rock.  You lose.")        
elif myInput == "paper":
    if compChoice == "scissors":
        print("Scissors cut paper.  You lose.")
elif myInput == "paper":
    if compChoice == "rock":
        print("Paper covers rock.  You win!.")
elif myInput == "scissors":
    if compChoice == "paper":
        print("Scissors cut paper.  You win!")
print("\n")  
#ask if you want to play again.
play_again = input("Play again? (y/n): ")
if play_again.lower() != "y":
    print("Ok, see you next time!")
    print("\n")

