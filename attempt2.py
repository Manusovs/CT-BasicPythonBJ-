from random import shuffle
player_list = ["dealer"]

class Deck:
    #I added a cards attribute, so we could have a list, with each
    def __init__(self, suit=[], numbers=[], cardset="", cards=[]):
        self.suit = suit
        self.numbers = numbers
        self.cardset = cardset
        self.cards = cards  # Change from cards = "" to cards = []

#Create a constructor method for each deck - each deck should have a defined suit,numbers, and sets
    def deck_constructor(self):
        for i in self.suit:
            for j in self.numbers:
                self.cards.append((i, j, self.cardset))

    #Create a method to get a deck of cards
    def get_deck(self): #pull current state of the deck.  
        print(self.cards)
    
    #Create method that will shuffle the deck   
    def shuffle_decks(self): #use the imported function
        shuffle(self.cards)

#Player with attributes        
class Player:
    
    def __init__(self, hand = [], score = 0): # I removed cards, because in Blackjack you don't keep cards outside of yourhand so I believe they are identical
        self.hand = hand
        self.score = score
    #Create a constructor for the player class that will hold the hand,cards,and tally the score

    def tally_score(self):
        print(f'{self.hand[-1][0]} this is the hand value')
        if self.hand[-1][0] == "Ace":
            self.score = self.score + 11
            if self.score > 21:
                self.score = self.score - 10
        elif self.hand[-1][0] == 11 or self.hand[-1][0] == 12 or self.hand[-1][0] == 13:
            self.score = self.score + 10     
        else:
            self.score = self.score + int(self.hand[-1][0])
        print(f'{self.score} this is the final score') # this is to visualize and check, possibly delete later
        return(self.score)
    
    # Get total score based on the hand the user/player is given
    def show_score(self):
        print(self.score)

    def bust_message(self):
       print(f"Sorry you busted with {self.score}.  Better luck next time")
    #Create a method to display a message if the user/player busts    

    def show_player_hand(self):
        print(self.hand)
        pass          
    #Create a method that will show the hand of the user/player

    def blackjack_message(self):
        print("Blackjack! Congratulations, collect your winnings")
    #Create a method displaying blackjack to the player        

    def win_message(self):
        print("Congratulations, you won!  Collect your winnings")          
    #Create a method displaying if the user wins
    

class Human(Player): #A Human should have characteristics of a player 
    # inheriting all the characteristics of Player
    def __init__(self, hand, score):
        super().__init__(hand, score) 

    def look_at_table(self):
        self.show_player_hand()
        print(f"Your current score is {self.score}")
        print(f"{Dealer.hand} this is the dealer's hand")
        print(f"Dealer's current score is {Dealer.score}")
    pass #Remove before starting
    #Define a constructor that has the characteristics of player
  
        
    #Display the Human as a player
    

class Dealer(Player):# A Human should have characteristics of a player (should this be a Dealer should have chars of a player)
    def __init__(self):
        super().__init__()
    # def __init__(self, hand, score):
    #     super().__init__(hand, score) 
        self.deck = Deck()
        # self.player = Player

    def player_constructor(self):
        # player_list = ["dealer"] # this may need to be a global list. 
        while True:
            player_name = input("What is the player's name? ") # in a more advanced version we should stop repeat player names
            active_player = Human([], 0)
            active_player.name = player_name #names the new player the requested name
            player_list.append(active_player)
            another_player = input("Would you like to add another player (yes or no)? ")
            if another_player.lower() != "yes":
                break
        print(f'the players are {player_list}')
        # for Name in player_name: # probably delete
        #     Name = Player # possibly switch this to self.player # probably delete
    #Define a constructor that has the characteristics of player
    def deal_hands(self,players): #this only allows for one player, but deals them at the same time as the dealer
        # active_player = players[1] #don't use 0 because that's the dealer
        for player in player_list:
            player.hand.append(self.deck.cards[0])
            self.deck.cards.pop(0) 
            print(f'Player drew {player.hand[-1][0]} of {player.hand[-1][1]}s')
        self.hand.append(self.deck.cards[0]) 
        self.deck.cards.pop(0)
        print(f'Dealer shows {self.hand[-1][0]} of {self.hand[-1][1]}')  
    #     active_player.hand.append(Deck[3][0]) 
    #     self.deck[3].pop(0)
    #     print(f'Player drew {splayer.hand[-1][0]} of {splayer.hand[-1][1]}s')
    #     self.hand.append(sdeck[3][0]) 
    #     self.deck[3].pop(0)
    #     splayer.hand.append(sdeck[3][0]) 
    #     self.deck[3].pop(0)
    #     print(f'Player drew {splayer.hand[-1][0]} of {splayer.hand[-1][1]}s')
    #     self.hand.append(sdeck[3][0]) 
    #     self.deck[3].pop(0)    
    #     print(f'Dealer shows {self.hand[-1][0]} of {self.hand[-1][1]}')    
    # #Define a method to deal the player a hand
    # def player_hit(self,splayer,sdeck):
    #         splayer.hand.append(sdeck[3][0]) 
    #         sdeck[3].pop(0)
    #         print(f'Player drew {splayer.hand[-1][0]} of {splayer.hand[-1][1]}s')
    #         splayer.tally_score()      
    #Define a method to give the player a hit if asked

    #Define a method that will tally and show the player ending hand #done in player
        
    #Display the Human as a Dealer (isn't the human not the dealer)
    

class Game:
    pass # Remove this before starting/running
    def __init__(self, dealer, human, players):
        self.dealer = dealer
        self.human = human
        self.players = players
    #Define a constructor that will have a dealer,human,and players(the dealer and the human)

    def winner_message(self):
        Player.win_message()
    #Define a method to display a message if the user/player wins

    def push_message(self):
        print("No winner, you pushed.  Would you like to try again?")                    
    #Define a method to display a message if the user/player pushes

    def loss_message(self):
        print("Sorry, you lose.  Better luck next time.")
    #Define a method to display a message if the user/player loses    

def main():
    pass #Remove when starting
    #Create game logic here
    
    #Create your class instances
    Scott = Human([], 0)
    Computer = Dealer()
    Blackjack = Game(Computer, Scott, [Computer, Scott])
    # DeckA = Deck(['Hearts', 'Diamonds', 'Clubs', 'Spades'], ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "A")
    MasterDeck = Deck()
    # Ask the player how many decks they want to use - Then print the number of decks
    deck_number = int(input("how many decks would you like to use? "))
    for i in range(deck_number):
        NewDeck = Deck()
        NewDeck.deck_constructor()
        MasterDeck.cards.append(NewDeck.cards)

    # Shuffle the deck
    MasterDeck.shuffle_decks()
    Computer.player_constructor()
    # Computer.deal_hands(Scott,MasterDeck)
    Computer.deal_hands(player_list)

    
    #HINT: Continue to ask player if they want a hit or if they want to end the game
    while action != "quit":
        action = input("Do you want to hit or stay? ")
        if action == "hit":
            Computer.player_hit(Scott, MasterDeck)
        #Ask the player if they want a hit
        #If they do, add the value of the card to their game tally
        #If they stand, keep the game tally where it is - add to dealer only
        elif action == "stay":
            action = "quit"
            print(f" the dealer's cards are \n {Computer[0].number} of {Computer[0].suit}\n {Computer[1].number} of {Computer[1].suit}")
            while Computer.score <16:
                if Computer.score > 21:
                    Blackjack.winner_message()
                else:
                    Computer.player_hit(Computer,MasterDeck)
            if Scott.score > Computer.score:
                Blackjack.winner_message()
            elif Scott.score < Computer.score:
                Blackjack.loss_message() 
            else:
                Blackjack.push_message()   
        #Also add to the tally of the dealer while their tally is less than 16
        #If the dealer and player tally are the same - display that result
        #If dealer wins - display that result
        #If player wins - display that result
# main()


MainDeck = Deck(['Hearts', 'Diamonds', 'Clubs', 'Spades'], ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "A")
MainDeck.deck_constructor()
# shuffle(MainDeck.cards)
Scott = Player([("Ace", "Spades","B")])
player_list.append(Scott)
print(type(player_list[-1].hand))
print(player_list[-1].hand)
player_list[-1].hand.append((3, "Hearts", "C"))
print(player_list[-1].hand)
print(MainDeck.cards[0])
player_list[-1].hand.append((MainDeck.cards[0]))
print(player_list[-1].hand)
player = player_list[-1]
print("player")
print(type(player.hand))
print(player.hand)
player.hand.append((3, "Hearts", "C"))
print(player.hand)
print(MainDeck.cards[0])
player.hand.append((MainDeck.cards[0]))
print(player.hand)
# Scott.tally_score()
# Scott.hand.append((11, "Diamonds","B"))
# Scott.tally_score()
# Scott.show_player_hand()
# MainDeck.get_deck()
# Scott.bust_message()
# Scott.blackjack_message()
# Scott.win_message()
