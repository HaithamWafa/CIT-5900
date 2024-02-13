# TODO: Students, fill out statement of work header
# Student Name in Canvas: Haitham Fawzi
# Penn ID: 61999177
# Did you do this homework on your own (yes / no): yes
# Resources used outside course materials: N/A
# import statements
import random
from random import shuffle
def get_user_input(question):
    '''
      Prompts the user with the given question and process the input.
      1. Returns the post-processed user input.
      2. Removes leading and trailing whitespaces.
      3. If the length of the user input after removing leading and trailing whitespaces is 0, reprompt.
      4. If the input is a number, casts and returns an integer type.
      5. If the input is a power card, returns the power card as an uppercase string.
      6. If the input is any other string, returns the string as a lowercase string.
    '''
    while(True):
        ans = input(question)
        ans = ans.strip() #removes leading and trailing whitespaces
        if(ans.isdigit()): #case: water card
            return int(ans) #casting if input is a number
        elif(ans.lower() == 'soh' or ans.lower() == 'dmt' or ans.lower() == 'dot'): #case: power card
            return ans.upper() #making it uppercase
        elif(len(ans) == 0): #case if the input is empty, it will re-prompt
            continue
        else:
            return ans.lower() #case: other string, makes it lowercase  
        
def setup_water_cards():
    '''
    1. Creats a shuffled list of water cards according to specs
    2. Returns the water cards as a list of integers.
    '''
    deck =  30 * [1] + 15 * [5] + 8 * [10] #setting up the deck
    shuffle(deck) #shuffling the deck
    return deck
def setup_power_cards():
    '''
    1. Creates a shuffled list of power cards according to specs
    2. Returns the power cards as a list of strings.
    '''
    deck = 10 * ['SOH'] + 2 * ['DOT'] + 3 * ['DMT'] #setting up the deck
    shuffle(deck) #shuffling the deck
    return deck
def setup_cards(): 
    '''
    1. Sets up both the water card and power card piles
    2. Returns a 2-tuple containing the water cards pile and the power cards pile, respectively (Each pile is represented by a list.)
    '''
    water_deck = setup_water_cards()
    power_deck = setup_power_cards()
    return water_deck, power_deck
def get_card_from_pile(pile, index):
     '''
     1. Removes the entry at the specified index of the given pile (water or power) and modifies the pile by reference.
     2. returns the entry at the specified index
     '''
     card = pile.pop(index)
     return card
def arrange_cards(cards_list):
    '''
    1. Arranges the players cards such that:
        a. The first three indices are water cards, sorted in ascending order.
        b. The last two indices are power cards, sorted in alphabetical order.
    2. This function doesn’t return anything
    '''
    water = []
    power = []
    for i in range(len(cards_list)):
      if(cards_list[i] in ['SOH', 'DOT', 'DMT'] ):
        power.append(cards_list[i])
      else:
        water.append(cards_list[i])

    water.sort()  #in-place sorting for water cards
    power.sort()  #in-place sorting for power cards
    arranged = water + power
    for i in range(len(cards_list)):
        cards_list[i] = arranged[i]

def deal_cards(water_cards_pile, power_cards_pile):
    '''
   1. Deals cards to player 1 and player 2. Each player would get 3 water cards and 2 power cards. Then, call the arrange_cards function to arrange the cards.
   2. When dealing, alternately takes off a card from the first entry in the pile
   3. Returns a 2-tuple containing the player 1’s hand and player 2’s hand, respectively. (Each hand is represented by a list.)
    '''
    player1_hand = []
    player2_hand = []
    #alternate player 1 hand and player 2 hand
    for i in range(3):
        player1_hand.append(water_cards_pile.pop(0))
        player2_hand.append(water_cards_pile.pop(0))
    for i in range(2):
        player1_hand.append(power_cards_pile.pop(0))
        player2_hand.append(power_cards_pile.pop(0))
    arrange_cards(player1_hand)
    arrange_cards(player2_hand)
    return player1_hand, player2_hand

def apply_overflow(tank_level):
    '''
    1. If necessary, apply the overflow rule: remaining water = maximum fill value - overflow
    2. Returns the tank level. If no overflow occurred, this is just the starting tank level (passed to the function)
    '''
    max = 80
    if (tank_level > max):
        overflow = tank_level - max #computing overflow
        remaining_water = max - overflow #applying penalty
        tank_level = remaining_water
    return tank_level
def check_pile(pile, pile_type):
    '''
    1. Checks if the given pile is empty. If so, call the pile’s setup function to replenish the pile.
    2. pile_type is a string to determine what type of pile you are checking (“water” or “power”)
    3. This function does not return anything
    '''
    if (len(pile) == 0): #checking empty pile
        if (pile_type == 'water'):
           pile[:] = setup_water_cards() #replinishing (changes list by reference)
        else: #assumed no programmatic error
           pile[:] = setup_power_cards()

def filled_tank(tank):
    '''
    Determines if the tank level is between the maximum and minimum fill values (inclusive).
    Return a boolean representing whether the tank is filled. 
    '''
    min = 75
    max = 80
    return min <= tank <= max #checks fill condition between 75 and 80

def use_card(player_tank, card_to_use, player_cards, opponent_tank):
    '''
    1. Gets that card from the player’s hand, and update the tank level based on the card that was used. 
    2. Apply overflow if necessary
    3. Returns a 2-tuple containing the player’s tank and the opponent’s tank, respectively.
    '''

    #applying power card policies
    if card_to_use == 'SOH':
        player_tank += opponent_tank//2
        opponent_tank= max(0, opponent_tank - opponent_tank//2)
    elif card_to_use == 'DOT':
        opponent_tank = 0
    elif card_to_use == 'DMT':
        player_tank *= 2
    else:
        player_tank += card_to_use

    player_cards.remove(card_to_use) #removes played card from hand
    player_tank = apply_overflow(player_tank) #checking overflow
    return player_tank, opponent_tank
def discard_card(card_to_discard, player_cards, water_cards_pile, power_cards_pile):
    '''
    1. Discard the given card from the player’s hand and return it to the bottom of the appropriate pile. 
    2. This function does not return anything
    '''
    player_cards.remove(card_to_discard) #removes discarded card from hand

    #adds discarded card to correct pile
    if (card_to_discard in ['SOH', 'DOT', 'DMT']):
        power_cards_pile.append(card_to_discard)
    else:
        water_cards_pile.append(card_to_discard)

def human_play(human_tank, human_cards, water_cards_pile, power_cards_pile, opponent_tank):
    '''
    1. Shows the human player’s water level and then the computer player’s water level.
    2. Shows the human player their hand and ask them if they want to use (‘u’) or discard (‘d’) a card. If the human player enters an invalid answer, reprompts until a valid answer is entered.
    3. Print the card the human player uses or discards. If the human player enters a card to use or discard which is not in their hand, reprompt until a valid card is entered.
    4. Once the human has used or discarded a card, draw a new card of the same type they just used/discarded.
    5. Makes sure that the human’s hand is still properly arranged after adding the new card.
    6. Print the new hand, the updated player’s and opponent’s tank levels.
    7. Returns a 2-tuple containing the human’s tank level and the computer’s tank level, respectively
    '''
    #printing stats
    print("Human's Tank Level:", human_tank)
    print("Computer's Tank Level:", opponent_tank)
    print("Human's Hand:", human_cards)
    ans = get_user_input("Do you want to use ('u') or discard ('d') a card? ")
    while(ans != 'u' and ans != 'd'):
      ans = get_user_input("please enter (u/d) only ")

    if ans == 'u': #using case
        card_to_use = get_user_input("Enter the card you want to use: ")
        while card_to_use not in human_cards:
            print("Invalid card. Please enter a valid card from your hand.")
            card_to_use = get_user_input("Enter the card you want to use: ")

        human_tank, opponent_tank = use_card(human_tank, card_to_use, human_cards, opponent_tank) #using chosen card
        print(f"Human used {card_to_use}.")
        if(card_to_use in ['SOH', 'DOT', 'DMT']):
          check_pile(power_cards_pile, 'power') #always checking pile before withdrawal to replenish it if needed
          new_card = get_card_from_pile(power_cards_pile,0)

        else:
          check_pile(water_cards_pile, 'water')
          new_card = get_card_from_pile(water_cards_pile,0)
        human_cards.append(new_card) #adding newly withdrawn card to human hand
        arrange_cards(human_cards) #arranging human hand after adding a new card
        print("New Hand:", human_cards)

#discarding case
    elif ans == 'd':
        card_to_discard = get_user_input("Enter the card you want to discard: ")
        while card_to_discard not in human_cards:
            print("Invalid card. Please enter a valid card from your hand.")
            card_to_discard = get_user_input("Enter the card you want to discard: ")

        discard_card(card_to_discard, human_cards, water_cards_pile, power_cards_pile)
        print(f"Human discarded {card_to_discard}.")
        if(card_to_discard in power_cards_pile):
          check_pile(power_cards_pile, 'power')
          new_card = get_card_from_pile(power_cards_pile,0)
        else:
          check_pile(water_cards_pile, 'water')
          new_card = get_card_from_pile(water_cards_pile,0)

        human_cards.append(new_card)
        arrange_cards(human_cards)
        print("New Hand:", human_cards)

    print("Updated Human's Tank Level:", human_tank)
    print("Updated Computer's Tank Level:", opponent_tank)
 
    return human_tank, opponent_tank


def computer_play(computer_tank, computer_cards, water_cards_pile, power_cards_pile, opponent_tank):  #computer strategy
    '''
    1. Similar to human_play, except that it has an algorithmic strategy to choose cards each turn
    2. Returns a 2-tuple containing the computer’s tank level and the human’s tank level, respectively
    '''

    temp = []
    if(1 in computer_cards and opponent_tank<20):  #discard condition (always discards the ones --> hoping for better cards)
      discard_card(1, computer_cards, water_cards_pile, power_cards_pile)
      print(f"Computer discarded {1}.")
      check_pile(water_cards_pile, 'water')
      new_card = get_card_from_pile(water_cards_pile, 0)

    else: #use condition
      #power card usage policy
      if('SOH' in computer_cards and opponent_tank > 20 ): #uses SOH if it has it and human has more than 20L
        card = 'SOH'
        computer_tank, opponent_tank = use_card(computer_tank, card, computer_cards, opponent_tank)
        print(f"Computer used {card}.")
        check_pile(power_cards_pile, 'power') #used before each withdrawal to replenish pile if empty before withdrawal
        new_card = get_card_from_pile(power_cards_pile, 0)

      elif('DOT' in computer_cards and opponent_tank > 30): #uses DOT if it has it and human has more than 30L
        card = 'DOT'
        computer_tank, opponent_tank = use_card(computer_tank, card, computer_cards, opponent_tank)
        print(f"Computer used {card}.")
        check_pile(power_cards_pile, 'power')
        new_card = get_card_from_pile(power_cards_pile, 0)
      elif('DMT' in computer_cards and computer_tank > 10): #uses DMT if it has it and computer has more than 10L
        card = 'DMT'
        computer_tank, opponent_tank = use_card(computer_tank, card, computer_cards, opponent_tank)
        print(f"Computer used {card}.")
        check_pile(power_cards_pile, 'power')
        new_card = get_card_from_pile(power_cards_pile, 0)

      else: #water card usage policy
        for i in range(len(computer_cards)):
          if(computer_cards[i] not in ['SOH', 'DOT', 'DMT']): #filtering water cards loop
            temp.append(computer_cards[i])
        card = max(temp) #playing the max water card available
        computer_tank, opponent_tank = use_card(computer_tank, card, computer_cards, opponent_tank)
        print(f"Computer used {card}.")
        check_pile(water_cards_pile, 'water')
        new_card = get_card_from_pile(water_cards_pile, 0)

    computer_cards.append(new_card) #adding new card to computer cards
    arrange_cards(computer_cards) #arranging computer cards after withdrawing a card
    #print("the computer cards are: ", computer_cards) #used for debugging


    print("Updated Computer's Tank Level:", computer_tank)
    print("Updated Opponent's Tank Level:", opponent_tank)

    return computer_tank, opponent_tank

def main():
    #initialzing tanks
    human_tank = 0
    computer_tank = 0
    #setting up decks
    water_pile, power_pile = setup_cards()
    #choosing a player at random in the beginning
    current_player = random.choice(["human", "computer"])
    #distributing cards for first round
    human_cards, computer_cards = deal_cards(water_pile, power_pile)

    #game starts
    while (True):

        print("******* New Turn *******")
        if current_player == "human":
            human_tank, computer_tank = human_play(human_tank, human_cards, water_pile, power_pile, computer_tank) #prompts user for strategy
            if (filled_tank(human_tank)): #condition of human winning
               print("******* Human Won *******")
               print("Final Human's Tank Level:", human_tank) #printing winner tank level
               break #breaking the game
            else:
              current_player = "computer" #alternating the turns
        else:
            computer_tank, human_tank = computer_play(computer_tank, computer_cards, water_pile, power_pile, human_tank) #executes algorithmic strategy
            if (filled_tank(computer_tank)):
              print("******* Computer Won *******")
              print("Final Computer's Tank Level:", computer_tank)
              break
            else:
              current_player = "human"
if __name__ == '__main__':
    main()
