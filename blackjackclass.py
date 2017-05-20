# -*- coding: utf-8 -*-
"""
Created on Fri May 19 21:33:07 2017
Classes for a Black Jack  Casino Game
@author: iibanez
"""

from numpy import random
class deck(object):
    '''
    class which defines and initializes the deck of 52 cards
    in four sub decks: 
        Hearts
        Diamonds
        Clovers
        Pikes
    Deck elements have the Subdeck name, followed by the card number:
        Ace, 2-10, J, Q, K
    Example: pike 11
    '''
    def __init__(self):
        standard =['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        deck = []
        for card in standard:
            temp = 'heart ' + card
            deck.append(temp)
            temp = 'diamond ' + card
            deck.append(temp)
            temp = 'clover ' + card
            deck.append(temp)
            temp = 'pike ' + card
            deck.append(temp)
        self.deck = deck
    def shuffle(self):
        random.shuffle(self.deck)
        
        


class player(object):
    '''
    Class for the Game players,
    Attributes:
        bankroll: money in possesion of the player
        bankrupcy: boolean which indicates if the player have debts...
    Methods:
        add_bankroll : adds the amount to the player bankroll
        substract_bankroll : substract the amount from the player bankroll
                            and checks if the player is in bankrupcy
        get_credit: buys new credit for the player, and checks if he/she is
                    not in bankrupcy anymore
    '''
    
    def __init__(self, bankroll=100):
        self.bankroll = bankroll
        self.bankrupcy = False
    
    def add_bankroll(self, amount):
        self.bankroll += amount
    
    def substract_bankroll(self, amount):
        self.bankroll -= amount
        if self.bankroll < 0:
            print 'Player has no funds!'
            self.bankrupcy = True
            
    def get_credit(self, amount):
        self.bankroll += amount
        if self.bankroll > 0:
            print 'Player has bought enough credit to continue!'
            self.bankrupcy = False
        

class game(object):
    '''
    class for the games to be played
    Attributes:
        
    Methods:
        
    '''
    def __init__(self, p_name, p_bet):
        self.player = p_name
        self.p_bet = p_bet
        self.p_cards =[]
        self.p_value = 0
        self.dealer = "house"
        self.d_cards =[]
        self.d_value = 0
        self.deck =deck()
        self.deck.shuffle()
        print ' The Cards are generated and shuffled'
        print ' the house and %s are in play' %(self.player)
    
    def take_card(self,turn):
        '''
        Depending on who is taking the card (H: House or P: Player)
        the method pops off one element of the SHUFFLED deck, and finds out their
        value. if its and ACE, the player (or the House) is asked for the value, 1 or 11
        the answer is only accepted when its 1 or 11
        '''
        if turn == "P":
            temp = self.deck.deck.pop()
            temp = temp.split()
            if temp[1] in ['J','Q','K']:
                self.p_value += 10
            elif temp[1] == 'Ace':
                rawinput = None
                while rawinput not in [1,11]:
                    try:
                        rawinput = int(raw_input('Please, Choose the value of the Ace, 1 or 11?  '))
                    except:
                        print 'That is not a valid option, the only possible values are 1 or 11'
                    finally:
                        if rawinput not in [1,11]:
                            print 'That is not a valid option, the only possible values are 1 or 11'
                self.p_value += int(rawinput)
            else:
                self.p_value += int(temp[1])
            print ' The Accumulated hand of the player is %i' %self.p_value
        elif turn == "H":
            temp = self.deck.deck.pop()
            temp = temp.split()
            if temp[1] in ['J','Q', 'K']:
                self.d_value += 10
            elif temp[1] == 'Ace':
                rawinput = None
                while rawinput not in [1,11]:
                    try:
                        rawinput = int(raw_input('Please, Choose the value of the Ace, 1 or 11?  '))
                    except:
                        print 'That is not a valid option, the only possible values are 1 or 11'
                    finally:
                        if rawinput not in [1,11]:
                            print 'That is not a valid option, the only possible values are 1 or 11'
                self.d_value += int(rawinput)
            else:
                self.d_value += int(temp[1])
            print ' The Accumulated hand of the House is %i' %self.d_value
            
        
        
    


cartas =deck()
#
##for i in cartas.deck:
##    print i
##print len(cartas.deck)
#
#cartas.shuffle()
#prueba =cartas.deck.pop()
#prueba = prueba.split()
#print prueba
#print len(cartas.deck)


juego = game('Bruno',20)

juego.take_card('P')
print juego.p_value
juego.take_card('P')
print juego.p_value