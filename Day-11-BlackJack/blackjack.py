############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################
from art import logo
import random

def play_blackjack():
  print(logo)

  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

  p_first_card = cards[random.randint(0, 12)]
  p_second_card = cards[random.randint(0, 12)]
  d_first_card = cards[random.randint(0, 12)]
  d_second_card = cards[random.randint(0,12)]

  player_cards = [p_first_card, p_second_card]
  dealer_cards = [d_first_card, d_second_card]
  player_score = p_first_card + p_second_card
  dealer_score = d_first_card + d_second_card

  if(player_score == 21 and dealer_score != 21):
    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Computer's final hand: {dealer_cards}, final score: {dealer_score}")
    print("You win with blackjack!")
  elif(dealer_score == 21 and player_score != 21):
    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Computer's final hand: {dealer_cards}, final score: {dealer_score}")
    print("Dealer got blackjack. You lose!")  
  elif(dealer_score == 21 and player_score == 21):
    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Computer's final hand: {dealer_cards}, final score: {dealer_score}")
    print("You both got blackjack and tied! It's a push")
  else:
    print(f"Your cards: {player_cards}, current score: {player_score}")
    print(f"Computer's first card: {d_first_card}")
    another_card = input("Type 'y' to get another card, type 'n' to pass: ")

    while another_card == 'y':
      next_player_card = cards[random.randint(0, 12)]
      player_cards.append(next_player_card)
      player_score += next_player_card
      if (player_score > 21):
        another_card = 'n'
      else:
        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Computer's first card: {d_first_card}") 
        another_card = input("Type 'y' to get another card, type 'n' to pass: ")

    while dealer_score < 17:
      next_dealer_card = cards[random.randint(0, 12)]
      dealer_cards.append(next_dealer_card)
      dealer_score += next_dealer_card
      if (dealer_score > 21):
        for card in range(len(dealer_cards)):
          if (dealer_cards[card] == 11):
            dealer_cards[card] = 1
            dealer_score -= 10
            break 
    
    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Computer's final hand: {dealer_cards}, final score: {dealer_score}")

    if player_score > 21:
      print("You went over. You lose")
    elif player_score < dealer_score and dealer_score < 22:
      print ("You lose.")
    elif dealer_score > 21:
      print("Opponent went over. You win! :)")
    elif player_score > dealer_score:
      print("You win! :))")
    else:
      print("You pushed!")

  play_again = input("Do you want to play again? Type 'y' or 'n': ")

  if play_again == 'y':
    play_blackjack()

play_blackjack()