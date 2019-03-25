import Gameplay
import Person

print("Welcome to BlackJack Game World!!!")
user_input = input("Wanna Gambling? \nPress 's' to Start / 'e' to Exit >>> ")
if user_input == 's':
    while True:
        cards = Gameplay.card()
        deck = Gameplay.deck_key()
        player = Person.Player()
        dealer = Person.Dealer()
        Gameplay.give_2cards(player.hand, dealer.hand, deck)
        print("Player's hand = ", player.hand)
        if player.over_21() == False or dealer.over_21() == False:
            pass
        else:
            while True:
                if player.decision(deck) == False:
                    break
                if player.over_21() == False:
                    break
            while True:
                if dealer.decision(deck) == False:
                    break
                if dealer.over_21() == False:
                    break
        Gameplay.outcome(player.score(), dealer.score())  
        Gameplay.close_game(dealer.score())  
elif user_input == 'e':
    print("Thank you for playing! Hope to see you again!")
    exit()
else:
    print("Wrong Insert. Please give me proper command.")
    exit()
