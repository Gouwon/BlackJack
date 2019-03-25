from random import shuffle


def card():
    pattern = ['S', 'C', 'H', 'D']
    numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    point = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '10', '10', '10', '11'] * 4
    card_form = []
    card_set = dict()
    for i in pattern:
        for v in numbers:
            card_form.append(i + v)
    for x in range(52):
        card_set[card_form[x]] = point[x]
    return card_set


def deck_key():
    deck_card = dict()
    deck_keys = []
    deck_card = card()
    deck_keys = list(deck_card.keys())
    shuffle(deck_keys)
    return deck_keys


def give_2cards(player_hand, dealer_hand, deck):
    for i in range(2):
        player_hand.append(deck.pop())
        dealer_hand.append(deck.pop())
    print("Dealer's hand = {}".format(dealer_hand[0]))


def outcome(player_hand, dealer_hand):
    print("..............Dealer's score =", dealer_hand)
    if player_hand < 21 and dealer_hand < 21:
        if player_hand == dealer_hand:
            print("Draw!")
        elif player_hand > dealer_hand:
            print("Player won the game!")   
        else:
            print("Player lost the game!")
    elif player_hand == 21:
        print("Player won the game!")
    elif dealer_hand == 21:
        print("Player lost the game!")
    elif player_hand < 21 and dealer_hand > 21:
        print("Player won the game!")
    elif player_hand > 21 and dealer_hand < 21:
        print("Player lost the game!")
    else:
        pass


def close_game(dealer_hand):
    user_input = input("Would you like to continue the game??\nPress 'r' to resume or 'q' to quit >>> ")
    if user_input == 'r':    
        return True
    elif user_input == 'q':
        print("Thank you for playing!")
        exit()
    else:
        print("Please check your Key!") 
        return close_game(dealer_hand)
    
