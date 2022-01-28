import art
import random
import replit
from game_data import data

def play_game ():
  game_winning = True
  score = 0

  player_a = data[random.randint(0,len(data) - 1)]
  player_b = data[random.randint(0, len(data) - 1)]

  while game_winning:
    print(art.logo)
    print(f"Compare A: {player_a['name']}, a {player_a['description']}, from {player_a['country']}.")
    print(art.vs)
    print(f"Compare B: {player_b['name']}, a {player_b['description']}, from {player_b['country']}.")
    choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    print(choice)
    higher_followers = "none"
    if (player_a["follower_count"] > player_b["follower_count"]):
      higher_followers = "a"
    else:
      higher_followers = "b"
    print(higher_followers)
    if choice == higher_followers:
      score += 1
      player_a = player_b
      # if same player chosen, loop until different player is chosen
      while (player_a == player_b):
        player_b = data[random.randint(0, len(data) - 1)]
    else:
      game_winning = False
    replit.clear()

  print(art.logo)
  print(f"Sorry, that's wrong. Final Score: {score}")

play_game()