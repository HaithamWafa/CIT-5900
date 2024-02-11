# TODO: Students, fill out statement of work header
# Student Name in Canvas: Haitham Fawzi
# Penn ID: 61999177
# Did you do this homework on your own (yes / no): yes
# Resources used outside course materials: N/A
# import statements
from random import shuffle
def get_user_input(question):
    ans = input(question)
    ans.strip()
    while(len(ans) == 0):
         ans = input(question)
         ans.strip()
    if(ans.isnumeric()): #case: water card
        return int(ans)
    elif(ans == 'soh' or ans == 'dmt' or ans == 'dot'): #case: power card
        return ans.upper()
    else:
        return ans.lower() #case: other string 
def setup_water_cards():
    deck =  30 * [1] + 15 * [5] + 8 * [10] #setting up the deck
    shuffle(deck) #shuffling the deck
    return deck
def setup_power_cards():
    deck = 10 * ['SOH'] + 2 * ['DOT'] + 3 * ['DMT']
    shuffle(deck)
    return deck
def setup_cards():
    water_deck = setup_water_cards()
    power_deck = setup_power_cards()
    return water_deck, power_deck
def get_card_from_pile(pile, index):
     card = pile.pop(index)
     return card
def arrange_cards(cards_list):
    water = cards_list[0:3]
    power = cards_list[3:5]
    water.sort()  #in-place sorting for water cards
    power.sort()  #in-place sorting for power cards
    cards_list = water + power

def deal_cards(water_cards_pile, power_cards_pile):
    player1_hand = []
    player2_hand = []
    #player 1 hand
    for i in range(3):
        player1_hand.append(water_cards_pile.pop(0))
    for i in range(2):
        player1_hand.append(power_cards_pile.pop(0))
    #player 2 hand
    for i in range(3):
        player2_hand.append(water_cards_pile.pop(0))
    for i in range(2):
        player2_hand.append(power_cards_pile.pop(0))
    
    return player1_hand, player2_hand

def apply_overflow(tank_level)
def use_card(player_tank, card_to_use, player_cards, opponent_tank):
def discard_card(card_to_discard, player_cards, water_cards_pile, power_cards_pile):
def filled_tank(tank):
def check_pile(pile, pile_type):
def human_play(human_tank, human_cards, water_cards_pile, power_cards_pile, opponent_tank):  
def computer_play(computer_tank, computer_cards, water_cards_pile, power_cards_pile,
opponent_tank):
def main():
# TODO: Write your code as described in the instructions
    pass
if __name__ == '__main__':
    main()
