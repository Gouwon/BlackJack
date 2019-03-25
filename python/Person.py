import Gameplay
class Person:
    def __init__(self):
        self.name = ''
        self.hand = []
        self.point = []

    def score(self):
        self.point = []
        for i in self.hand:
            cards = Gameplay.card()  
            k = cards[i]
            self.point.append(int(k))
        a = sum(self.point)

        if a > 21 and self.point.count(11) != 0: 
            total_value = sum(self.point)
            a_value = self.point.count(11)
            a = total_value - (a_value * 10)
            return int(a)

        elif a > 21 and self.point.count(11) == 0:
            return int(a)
        elif a < 21:
            return int(a)   
        else:
            return int(a)     
        
    def over_21(self):  
        score = self.score()
        if score > 21:
            print("{} has busted!".format(self.name))
            return False
        elif score == 21:
            print("Congratulations! {} has accomplished BlackJack!".format(self.name))
            return False
        else:
            return True

######################### Player #######################

class Player(Person):
    def __init__(self):
        super().__init__()
        self.name = "Player"
        print("{} has entered the game.".format(self.name))

    def decision(self, player_hand):
        user_input = input("Hit or Stay??? \n'h' for Hit, 's' for Stay >>> ")
        if user_input == 'h':
            self.hand.append(player_hand.pop())
            print("{}'s hand = {}".format(self.name, self.hand))
            return True
        elif user_input == 's':
            return False
        else:
            print("Please re-check your insert key!!")
            return self.decision(player_hand)

    def score(self):
        a = super().score()
        print("..............{}'s score = {}".format(self.name, a))
        return a

######################### Dealer #######################

class Dealer(Person):
    def __init__(self):
        super().__init__()
        self.name = "Dealer"
        print("{} has entered the game.".format(self.name))

    def decision(self, dealer_hand):        
        if self.score() > 17:
            return False
        else:
            self.hand.append(dealer_hand.pop())
            return True
