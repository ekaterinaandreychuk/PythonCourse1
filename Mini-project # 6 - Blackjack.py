# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}



# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos, draw_back_card):
        if draw_back_card == True:
            card_loc = (CARD_BACK_CENTER[0], 
                    CARD_BACK_CENTER[1])
            canvas.draw_image(card_back, card_loc, CARD_BACK_SIZE, [pos[0] + CARD_BACK_CENTER[0], pos[1] + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)          	
        else:
            card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
            canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)       
        
# define hand class
class Hand:
    def __init__(self):
        self.list_of_cards = []
        # create Hand object
             
    def __str__(self):
        list = ""
        for i in range(len(self.list_of_cards)):
            list += " " + str(self.list_of_cards[i])
        return "Hand contains" + list	# return a string representation of a hand

    def add_card(self, card):
        self.list_of_cards.append(card)
            # add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        value = 0
        has_aces = False
        for card in self.list_of_cards:
            if card.get_rank == 'A':
                has_aces = True
            value += VALUES[card.get_rank()]      
        if has_aces == False:
            return value
        else:
            if value + 10 <= 21:
                return value + 10
            else:
                return value
        # compute the value of the hand, see Blackjack video
   
    def draw(self, canvas, pos, hide_first_card):
        for i in range(len(self.list_of_cards)):
            if hide_first_card == True and i == 0:
                self.list_of_cards[i].draw(canvas, pos, True)
            else:
                self.list_of_cards[i].draw(canvas, pos, False)
            pos[0] += CARD_SIZE[0] + 10
        # draw a hand on the canvas, use the draw method for cards
 
        
# define deck class 
class Deck:
    def __init__(self):
        self.list_of_cards = []
        for suit in SUITS:
            for rank in RANKS:
                c = Card(suit, rank) 
                self.list_of_cards.append(c)
                # create a Deck object
               
    def shuffle(self):
        # shuffle the deck 
        return random.shuffle(self.list_of_cards)    # use random.shuffle()
        

    def deal_card(self):
        return self.list_of_cards.pop(0) # deal a card object from the deck
    
    def __str__(self):
        list = ""
        for i in range(len(self.list_of_cards)):
            list += " " + str(self.list_of_cards[i])
        return "Deck contains" + list	# return a string representing the deck

my_deck = Deck()
player = Hand()
dealer = Hand()

#define event handlers for buttons
def deal():
    global outcome, in_play, my_deck, player, dealer, score
    my_deck = Deck()
    player = Hand()
    dealer = Hand()
    if in_play == True:
        outcome = "You have lost. Hit or Stand?"
        score -= 1
    else:
        outcome  = "Hit or stand?"

    # your code goes here
    in_play = True
    my_deck.shuffle()
    player.add_card(my_deck.deal_card())
    player.add_card(my_deck.deal_card())
    dealer.add_card(my_deck.deal_card())
    dealer.add_card(my_deck.deal_card())
    print "Player has " + str(player)
    print "Dealer has " + str(dealer)
    

def hit():
        # replace with your code below
    global outcome, in_play, my_deck, player, dealer, score
    if in_play == True:
        value = player.get_value()
        if value <= 21:
            player.add_card(my_deck.deal_card())
            value = player.get_value()
        if value > 21:
            outcome = "You have busted. New deal?"
            in_play = False
            score -= 1
        
    # if the hand is in play, hit the player
   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global outcome, in_play, my_deck, player, dealer, score
    # replace with your code below
    
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score
    if in_play == True:
        value = player.get_value()
        in_play = False
        if value > 21:
            outcome = "You have busted. New deal?"
            score -= 1
        else:
            dealer_value = dealer.get_value()
            while dealer_value <= 17:
                dealer.add_card(my_deck.deal_card())
                dealer_value = dealer.get_value()
            if dealer_value > 21:
                outcome = "Dealer has busted. New deal?"
                score += 1
            elif value <= dealer_value:
                outcome = "Dealer wins. New deal?"
                score -= 1
            else:
                outcome = "Player wins. New deal?"
                score += 1
    
# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text("Blackjack", [290, 50], 24, "White")
    canvas.draw_text("Player", [50, 110], 24, "White")
    canvas.draw_text("Dealer", [50, 260], 24, "White")
    canvas.draw_text(str(outcome), [290, 100], 24, "White")
    canvas.draw_text("Score " + str(score), [450, 120], 24, "Blue")
    player.draw(canvas, [50, 120], False)
    dealer.draw(canvas, [50, 270], in_play)
    


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric