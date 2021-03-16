from core_functions import rnd, clr, slp
from game_ui import place_bets_ui, setup_ui, setup_ui2, first_turn_ui, player_turn_ui, dealer_turn_ui, end_game_ui, default_table_message, blackjack_message, player_win_message, player_bust_message, dealer_win_message, dealer_bust_message, push_message

# ==== GENERATE DECK ====

class Card:
    def __init__(self, rank, suit, value):
        self.rank = rank,
        self.suit = suit,
        self.value = value
        
values = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10, "A":11}

suits = ["\u2664", "\u2665", "\u2666", "\u2667"]

deck = []

for suit in suits:
    for value in values:
        deck.append(Card(value, suit, values[value]))

# ==== GENERATE & RANDOMIZE SHOE ====

shoe = deck * 6

def shuffle():
    rnd.shuffle(shoe)

# ==== SET DEFAULT VALUES ====

user = {"name":"Guest", "password":"Guest", "bank":100000} # DEFAULT USER DATA

user_bank = user["bank"]

dealer_hand = []
player_hand = []
player_hand2 = []

dealer_hand_total = 0
player_hand_total = 0

discard_pile = []

bet = 0

# ==== DISCARD HANDS ====

def discard():
    global player_hand
    global dealer_hand
    global discard_pile
    while len(player_hand) > 0:
        discard_pile.append(player_hand.pop())
    while len(dealer_hand) > 0:
        discard_pile.append(dealer_hand.pop())

# ==== VALIDATE BETS ====

def validate_bet(bank, valid_inputs, ui):
    print()
    inp = input("Place your bet: ")
    while True:
        if int(inp) in valid_inputs and int(inp) <= bank:
            return int(inp)
        elif int(inp) in valid_inputs and int(inp) > bank:
            clr()
            ui(bank, default_table_message)
            print()
            inp = int(input("Bet exceeds available funds. Please try again: "))
        else:
            clr()
            ui(bank, default_table_message)
            print()
            inp = int(input("Invalid selection. Please try again: "))
            continue

# ==== PLACE BETS ====

def place_bets(bank):
    global bet
    global user_bank
    place_bets_ui(bank, default_table_message)
    player_bet = validate_bet(bank, [10, 25, 50, 100, 250, 500, 1000], place_bets_ui)
    user_bank -= player_bet
    bet = player_bet

# ==== CREATE TABLE FOR PLAY & TRACK NEW VALUES ====

for card in player_hand:
    player_hand_total = card.value
    
for card in dealer_hand:
    dealer_hand_total = card.value

def deal():
    global player_hand_total
    global dealer_hand_total
    
    setup_ui(user_bank, dealer_hand, player_hand, dealer_hand_total, player_hand_total, default_table_message)
    player_hand.append(shoe.pop())
    player_hand_total += player_hand[-1].value

    setup_ui(user_bank, dealer_hand, player_hand, dealer_hand_total, player_hand_total, default_table_message)
    dealer_hand.append(shoe.pop())
    dealer_hand_total += dealer_hand[-1].value
    
    setup_ui(user_bank, dealer_hand, player_hand, dealer_hand_total, player_hand_total, default_table_message)
    player_hand.append(shoe.pop())
    if player_hand[0].value==11 and player_hand[1].value==11:
        player_hand_total += 1
    else:
        player_hand_total += player_hand[1].value

    setup_ui(user_bank, dealer_hand, player_hand, dealer_hand_total, player_hand_total, default_table_message)
    dealer_hand.append(shoe.pop())
    dealer_hand_total += dealer_hand[-1].value

    setup_ui2(user_bank, dealer_hand, player_hand, dealer_hand_total, player_hand_total, default_table_message)

# ==== DEFINE EACH TURN ====

def player_turn():
    player_turn_ui(user_bank, dealer_hand, player_hand, dealer_hand_total, player_hand_total, default_table_message)
    player_input=player_input_validation([1, 2], player_turn_ui)
    if player_input == 1:
        hit()
    if player_input == 2:
        stand()

def dealer_turn():
    if dealer_hand_total < 17:
        dealer_turn_ui(user_bank, dealer_hand, player_hand, dealer_hand_total, player_hand_total, default_table_message)
        dealer_hit()
    else:
        dealer_stand()

# ==== DEFINE USER INPUT OUTCOMES ====

def hit(): ################################################ FIX SOFT VALUES ###############################################################
    global player_hand_total
    card = shoe.pop()
    if card.value == 11 and player_hand_total > 10:
        player_hand.append(card)
        player_hand_total += 1
    else:
        player_hand.append(card)
        player_hand_total += player_hand[-1].value
    if player_hand_total > 21:
        player_bust()
    else:
        player_turn()

def stand():
    dealer_turn()

def double():
    global bet
    global user_bank
    global player_hand_total
    user_bank -= bet
    bet *= 2
    player_hand.append(shoe.pop())
    player_hand_total += player_hand[-1].value
    dealer_turn()

def split():
    pass

# ==== DEFINE DEALER CHOICES ====

def dealer_hit():
    global dealer_hand_total
    card = shoe.pop()
    if card.value == 11 and dealer_hand_total > 10:
        dealer_hand.append(card)
        dealer_hand_total += 1
    else:
        dealer_hand.append(card)
        dealer_hand_total += dealer_hand[-1].value
    if dealer_hand_total > 21:
        dealer_bust()
    else:
        dealer_turn()

def dealer_stand():
    global player_hand_total
    global dealer_hand_total
    if player_hand_total > dealer_hand_total:
        player_win()
    elif dealer_hand_total > player_hand_total:
        dealer_win()
    else:
        push()

# ==== DEFINE GAME OUTCOMES ====

def blackjack():
    global user_bank
    user_bank += bet+bet//3*2
    user["bank"] = user_bank
    end_game_ui(user_bank, dealer_hand, player_hand, dealer_hand_total, player_hand_total, blackjack_message)
    discard()

def player_win():
    global user_bank
    user_bank += bet*2
    end_game_ui(user_bank, dealer_hand, player_hand, dealer_hand_total, player_hand_total, player_win_message)
    discard()

def player_bust():
    user["bank"] = user_bank
    end_game_ui(user_bank, dealer_hand, player_hand, dealer_hand_total, player_hand_total, player_bust_message)
    discard()

def dealer_win():
    user["bank"] = user_bank
    dealer_turn_ui(user_bank, dealer_hand, player_hand, dealer_hand_total, player_hand_total, default_table_message)
    end_game_ui(user_bank, dealer_hand, player_hand, dealer_hand_total, player_hand_total, dealer_win_message)
    discard()

def dealer_bust():
    global user_bank
    user_bank += bet*2
    user["bank"] = user_bank
    dealer_turn_ui(user_bank, dealer_hand, player_hand, dealer_hand_total, player_hand_total, default_table_message)
    end_game_ui(user_bank, dealer_hand, player_hand, dealer_hand_total, player_hand_total, dealer_bust_message)
    discard()

def push():
    global user_bank
    user_bank += bet
    user["bank"] = user_bank
    end_game_ui(user_bank, dealer_hand, player_hand, dealer_hand_total, player_hand_total, push_message)
    discard()

# ==== DEFINE USER INPUT VALIDATIONS ====

def player_input_validation(valid_inputs, ui):
    print()
    inp = input("Select option: ")
    while True:
        if int(inp) in valid_inputs:
            return int(inp)
        else:
            clr()
            ui(user_bank, dealer_hand, player_hand, dealer_hand_total, player_hand_total, default_table_message)
            print()
            inp = int(input("Invalid selection. Please try again: "))
            continue

# ==== GET USER INPUT ====

def first_turn():
    global player_hand_total
    first_turn_ui(user_bank, dealer_hand, player_hand, dealer_hand_total, player_hand_total, default_table_message)
    if player_hand_total == 21:
        blackjack()
    valid_inputs=[1, 2, 3]
    if player_hand[0].value == player_hand[1].value:
        valid_inputs=[1, 2, 3, 4]
    player_input=player_input_validation(valid_inputs, first_turn_ui)
    if player_input == 1:
        hit()
    if player_input == 2:
        stand()
    if player_input == 3:
        double()
    if player_input == 4:
        split()

shuffle()
place_bets(user_bank)
deal()
first_turn()