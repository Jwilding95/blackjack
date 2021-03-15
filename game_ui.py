from core_functions import clr, slp

def setup_ui(bank, dealer_hand, player_hand, dealer_hand_total, player_hand_total, table_message):
    slp(.5)
    clr()
    print(f"Bank: {bank}")
    print()
    dealer_hand_cards = "               "
    for card in dealer_hand:
        dealer_hand_cards += "".join(card.rank + card.suit) + " "
    print(dealer_hand_cards)
    print(f"          Dealer Total: {dealer_hand_total}")
    print()
    print(f"{table_message}")
    print()
    player_hand_cards = "               "
    for card in player_hand:
        player_hand_cards += "".join(card.rank + card.suit) + " "
    print(player_hand_cards)
    print(f"          Player Total: {player_hand_total}")

def setup_ui2(bank, dealer_hand, player_hand, dealer_hand_total, player_hand_total, table_message):
    slp(.5)
    clr()
    print(f"Bank: {bank}")
    print()
    print("              ", "".join(dealer_hand[0].rank + dealer_hand[0].suit) + " []")
    print(f"          Dealer Total: {dealer_hand[0].value}")
    print()
    print(f"{table_message}")
    print()
    player_hand_cards = "               "
    for card in player_hand:
        player_hand_cards += "".join(card.rank + card.suit) + " "
    print(player_hand_cards)
    print(f"          Player Total: {player_hand_total}")

def first_turn_ui(bank, dealer_hand, player_hand, dealer_hand_total, player_hand_total, table_message):
    clr()
    print(f"Bank: {bank}")
    print()
    print("              ", "".join(dealer_hand[0].rank + dealer_hand[0].suit), "[]")
    print(f"          Dealer Total: {dealer_hand[0].value}")
    print()
    print(f"{table_message}")
    print()
    player_hand_cards = "               "
    for card in player_hand:
        player_hand_cards += "".join(card.rank + card.suit) + " "
    print(player_hand_cards)
    print(f"          Player Total: {player_hand_total}")
    print()
    if player_hand[0].value==player_hand[1].value:
        print("    [Hit] [Stand] [Double] [Split]")
        print("     [1]    [2]     [3]      [4]")
    else:
        print("       [Hit] [Stand] [Double]")
        print("        [1]    [2]     [3]")

def player_turn_ui(bank, dealer_hand, player_hand, dealer_hand_total, player_hand_total, table_message):
    clr()
    print(f"Bank: {bank}")
    print()
    print("              ", "".join(dealer_hand[0].rank + dealer_hand[0].suit), "[]")
    print(f"          Dealer Total: {dealer_hand[0].value}")
    print()
    print(f"{table_message}")
    print()
    player_hand_cards = "               "
    for card in player_hand:
        player_hand_cards += "".join(card.rank + card.suit) + " "
    print(player_hand_cards)
    print(f"          Player Total: {player_hand_total}")
    print()
    print("            [Hit] [Stand]")
    print("             [1]    [2]")

# def dealer_turn_ui(bank, dealer_hand, player_hand, dealer_hand_total, player_hand_total):
#     slp(.5)
#     clr()
#     print(f"Bank: {bank}")
#     print()
#     dealer_hand_cards = "               "
#     for card in dealer_hand:
#         dealer_hand_cards += "".join(card.rank + card.suit) + " "
#     print(dealer_hand_cards)
#     print()
#     print("        BLACKJACK PAYS 3 TO 2")
#     print("Dealer must draw to 16 and stand on 17")
#     print()
#     player_hand_cards = "               "
#     for card in player_hand:
#         player_hand_cards += "".join(card.rank + card.suit) + " "
#     print(player_hand_cards)
#     print(f"          Player Total: {player_hand_total}")
#     print()
#     print("             [Hit] [Stand]")
#     print("              [1]    [2]")

default_table_message = "        BLACKJACK PAYS 3 TO 2\nDealer must draw to 16 and stand on 17"