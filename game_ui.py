from core_functions import clr, slp

def place_bets_ui(bank, table_message):
    clr()
    print(f"Bank: {bank}")
    print("\n\n\n")
    print(f"{table_message}")
    print("\n\n\n")
    print("               BET AMOUNTS")
    print()
    print("[10]  [25]  [50]  [100]  [250]  [500]  [1000]")
    


def setup_ui(bank, dealer_hand, player_hand, dealer_hand_total, player_hand_total, table_message):
    slp(.5)
    clr()
    print(f"Bank: {bank}")
    print()
    dealer_hand_cards = "                  "
    for card in dealer_hand:
        dealer_hand_cards += "".join(card.rank + card.suit) + " "
    print(dealer_hand_cards)
    print(f"             Dealer Total: {dealer_hand_total}")
    print()
    print(f"{table_message}")
    print()
    player_hand_cards = "                  "
    for card in player_hand:
        player_hand_cards += "".join(card.rank + card.suit) + " "
    print(player_hand_cards)
    print(f"             Player Total: {player_hand_total}")

def setup_ui2(bank, dealer_hand, player_hand, dealer_hand_total, player_hand_total, table_message):
    slp(.5)
    clr()
    print(f"Bank: {bank}")
    print()
    print("                 ", "".join(dealer_hand[0].rank + dealer_hand[0].suit) + " []")
    print(f"             Dealer Total: {dealer_hand[0].value}")
    print()
    print(f"{table_message}")
    print()
    player_hand_cards = "                  "
    for card in player_hand:
        player_hand_cards += "".join(card.rank + card.suit) + " "
    print(player_hand_cards)
    print(f"             Player Total: {player_hand_total}")

def first_turn_ui(bank, dealer_hand, player_hand, dealer_hand_total, player_hand_total, table_message):
    clr()
    print(f"Bank: {bank}")
    print()
    print("                 ", "".join(dealer_hand[0].rank + dealer_hand[0].suit), "[]")
    print(f"             Dealer Total: {dealer_hand[0].value}")
    print()
    print(f"{table_message}")
    print()
    player_hand_cards = "                  "
    for card in player_hand:
        player_hand_cards += "".join(card.rank + card.suit) + " "
    print(player_hand_cards)
    print(f"             Player Total: {player_hand_total}")
    print()
    if player_hand[0].value==player_hand[1].value:
        print("       [Hit] [Stand] [Double] [Split]")
        print("        [1]    [2]     [3]      [4]")
    else:
        print("          [Hit] [Stand] [Double]")
        print("           [1]    [2]     [3]")

def player_turn_ui(bank, dealer_hand, player_hand, dealer_hand_total, player_hand_total, table_message):
    clr()
    print(f"Bank: {bank}")
    print()
    print("                 ", "".join(dealer_hand[0].rank + dealer_hand[0].suit), "[]")
    print(f"             Dealer Total: {dealer_hand[0].value}")
    print()
    print(f"{table_message}")
    print()
    player_hand_cards = "                  "
    for card in player_hand:
        player_hand_cards += "".join(card.rank + card.suit) + " "
    print(player_hand_cards)
    print(f"             Player Total: {player_hand_total}")
    print()
    print("               [Hit] [Stand]")
    print("                [1]    [2]")

def dealer_turn_ui(bank, dealer_hand, player_hand, dealer_hand_total, player_hand_total, table_message):
    slp(.75)
    clr()
    print(f"Bank: {bank}")
    print()
    dealer_hand_cards = "                  "
    for card in dealer_hand:
        dealer_hand_cards += "".join(card.rank + card.suit) + " "
    print(dealer_hand_cards)
    print(f"             Dealer Total: {dealer_hand_total}")
    print()
    print(f"{table_message}")
    print()
    player_hand_cards = "                  "
    for card in player_hand:
        player_hand_cards += "".join(card.rank + card.suit) + " "
    print(player_hand_cards)
    print(f"             Player Total: {player_hand_total}")
    print()


def end_game_ui(bank, dealer_hand, player_hand, dealer_hand_total, player_hand_total, table_message):
    slp(.75)
    clr()
    print(f"Bank: {bank}")
    print()
    dealer_hand_cards = "                  "
    for card in dealer_hand:
        dealer_hand_cards += "".join(card.rank + card.suit) + " "
    print(dealer_hand_cards)
    print(f"             Dealer Total: {dealer_hand_total}")
    print()
    print(f"{table_message}")
    print()
    player_hand_cards = "                  "
    for card in player_hand:
        player_hand_cards += "".join(card.rank + card.suit) + " "
    print(player_hand_cards)
    print(f"             Player Total: {player_hand_total}")
    print()

default_table_message = "           BLACKJACK PAYS 3 TO 2\n   Dealer must draw to 16 and stand on 17"

blackjack_message =     "                BLACKJACK!\n"

player_win_message =    "                 YOU WIN!\n"

player_bust_message =   "                YOU BUST!\n"

dealer_win_message =    "               DEALER WINS!\n"

dealer_bust_message =   "               DEALER BUST!\n"

push_message =          "                   PUSH\n"