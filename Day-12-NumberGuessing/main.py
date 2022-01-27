#Number Guessing Game Objectives:

# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
def game_play (difficulty, magic_number):
  win = False
  if difficulty == 'easy':
    tries = 10
  else:
    tries = 5

  while tries > 0:
    print(f"You have {tries} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess > magic_number:
      print("Number is too high!")
      tries -= 1
    elif guess < magic_number:
      print("Number is too low!")
      tries -= 1
    else:
      print(f"You got it! The answer is {magic_number}")
      win = True
      break
  
  if (win == False):
    print("You ran out of guesses, you lose!")

def run_game():
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100")
  magic_number = random.randint(1, 100)
  print(f"psst the magic number is {magic_number}")

  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
  game_play(difficulty, magic_number) 

run_game()