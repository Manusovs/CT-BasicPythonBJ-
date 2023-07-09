from random import shuffle


'''52 cards, 4 suits, 13 per suit
SHUFFLE 
deal 2 cards to player and dealer
player cards are all visible, 1st dealer card nonvisible
both bust beyond 21
option to hit or stand
player dealt 21 
highest wins'''

class Cards:
    '''Cards have 2 attributes a suit and a number
    suit is expected to be one of 4 strings "Heart", "Diamond", "Club", & "Spade"
    number is expecter to be an integer 1 -13'''
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit


# starting empty lists that we add to. 
deck= []
playercards = []
dealercards = []


# uses the Card object to build a 52 card deck (modify here, if you want to change the deck used)
def create_deck():
    for i in range(1,14):
        heartcard = Cards(i,"Heart") 
        diamondcard = Cards(i,"Diamond") 
        clubcard = Cards(i,"Club") 
        spadecard = Cards(i,"Spade") 
        deck.append(heartcard)
        deck.append(diamondcard)
        deck.append(clubcard)
        deck.append(spadecard)
        shuffle(deck)


#add a card to player hand, remove it from the deck, and reveal it
def playerdraw():
    playercards.append(deck[0]) 
    deck.pop(0)
    print(f'You drew {playercards[-1].number} of {playercards[-1].suit}s')

#add a card to dealer hand and remove it from the deck (not yet revealed)
def dealerdraw():
    dealercards.append(deck[0])
    deck.pop(0) 

# comes up with the current score for someone's hand
def score(cardlist):
    cardscore = 0
    for card in range(len(cardlist)):
        if cardlist[card].number == 1:
            cardscore = cardscore + 11
        elif cardlist[card].number == 11 or cardlist[card].number == 12 or cardlist[card].number == 13:
            cardscore = cardscore + 10     
        else:
            cardscore = cardscore + cardlist[card].number
    return(cardscore)   

# this adjusts the score to be the highest possible value without busting - relevant for aces   
def acescore(acehand):
    acescore = score(acehand)
    # this loop first checks if were over 21, then if it is it checks for Aces and reduces the score by 10
    for acard in range(len(acehand)):
        if acescore > 21:
            if acehand[acard].number == 1:
                acescore = acescore - 10
            #else pass isn't needed, but it helps track all the if statements easier.  
            else: 
                pass
    return(acescore)

# this is the final step and determine who wins if no one has already busted
def compare_scores(player,dealer):
    playerscore = acescore(player)
    dealerscore = acescore(dealer)
    if playerscore > dealerscore:
        message = "Congratulations, you win, collect your winnings"
    elif playerscore < dealerscore:
        message = "Better luck next time, dealer has " + str(dealerscore)
    else:
        message = "Push, you tied the dealer"
    return(message)
    
# run game
def blackjack():
    action = ""
    playerdraw()  
    dealerdraw()
    playerdraw() 
    dealerdraw()
    #Show the last card dealt to dealer
    print(f'The dealer has {dealercards[1].number} of {dealercards[1].suit}s showing')
    playerscore = acescore(playercards)
    dealerscore = acescore(dealercards)
    if playerscore == 21:
        print("Blackjack, you win, collect your winnings")
    else:
        while action != "quit":
            print(f' \nYour total is {playerscore};      The dealer has {dealercards[1].number} of {dealercards[1].suit}s showing')
            action = input("hit or stay ")
            if action.lower() == "hit":
                playerdraw()
                playerscore = acescore(playercards)
                if playerscore > 21:
                    print("you busted")
                    action = "quit"
                else: 
                    pass
            elif action.lower() == "stay":
                print(f" the dealer's cards are \n {dealercards[0].number} of {dealercards[0].suit}\n {dealercards[1].number} of {dealercards[1].suit}")
                while action != "quit": 
                    if dealerscore > 21:
                        print("dealer busted you win")
                        action = "quit"
                    elif dealerscore <= 16:
                        dealerdraw()
                        dealerscore = acescore(dealercards)
                        print(f'dealer hits and gets {dealercards[-1].number} of {dealercards[-1].suit}s')
                    else:
                        print(compare_scores(playercards,dealercards))
                        action = 'quit'
            else:
                print("\nPLEASE TYPE EITHER 'hit' OR 'stay'")


#Actually running the functions
create_deck()
blackjack()
# compare_scores(playercards,dealercards)