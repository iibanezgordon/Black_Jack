# -*- coding: utf-8 -*-
"""
Created on Fri May 19 21:33:07 2017
Classes for a Black Jack  Casino Game
The Games finished in a Tie return the money to the players 1:1
The games won by the player are 3:2 player reeives 3$ for each 2$ he /She bet
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
        
def validate_input(datatype, playerA=None):
    if datatype == 'string':
        while True:
            try:
                result = str(raw_input('Please, Introduce the Required input  '))
                break
            except:
                print 'That is not a valid option, please introduce a valid input'
        return result
    elif datatype == 'integer':
        while True:
            try:
                result = int(raw_input('Please, Introduce the Required input  '))
                break
            except:
                print 'That is not a valid option, please introduce a valid input'
        return result
    elif datatype == 'Y/N':
        while True:
            try:
                result = raw_input(' (Y/N)  ')
                if result == 'Y' or result == 'N':
                    break
                else:
                    raise
            except:
                print 'That is not a valid option, please introduce a valid input'
        return result
    elif datatype == 'credit':
        while True:
            try:
                result = int(raw_input(':  ' ))
                if result <= playerA.bankroll:
                    break
                else:
                    raise
            except:
                    print ' Sorry, answer not valid, must be an integer number of Bitcoins'
                    print ' You need to have enough funds to bet'
        return result
    elif datatype == 'bankrupt':
        while True:
            try:
                result =int(raw_input('Please, Introduce additional credit or 0 for denial  '))
                check =isinstance(result, ( int, long))
                if check == True:
                    break
                else:
                    raise
            except:
                   print 'That is not a valid option, please introduce an Integer'
        return result

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
    
    def __init__(self, p_name, bankroll=100):
        self.p_name = p_name
        self.bankroll = bankroll
        if self.bankroll > 0:
            self.bankrupcy = False
        else:
            self.bankrupcy = True
    
    def add_bankroll(self, amount):
        self.bankroll += amount
        if self.bankroll > 0:
            self.bankrupcy = False
    
    def substract_bankroll(self, amount):
        self.bankroll -= amount
        if self.bankroll <= 0:
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
        self.p_hit = True
        self.dealer = "house"
        self.d_cards =[]
        self.d_value = 0
        self.d_hit = True
        self.deck =deck()
        self.deck.shuffle()
        print ' The Cards are generated and shuffled'
        print ' the house and %s are in play' %(self.player)
        
    def show_cards(self):
        '''
        Method that prints out the cards of the Player or the House
        '''
        print ' The cards hold by %s:\n\n' %self.player
        for i in self.p_cards:
            print i
            print '\n'
        print ' %s holds a value of %i\n\n' %(self.player, self.p_value)
        print ' The cards hold by the House:\n\n' 
        for i in self.d_cards:
            print i
            print '\n'
        print ' The House holds a value of %i\n\n' %self.d_value
                
            
        
        
    
    def take_card(self,turn):
        '''
        Depending on who is taking the card (H: House or P: Player)
        the method pops off one element of the SHUFFLED deck, and finds out their
        value. if its and ACE, the player (or the House) is asked for the value, 1 or 11
        the answer is only accepted when its 1 or 11
        '''
        
        if turn == "P":
            temp = self.deck.deck.pop()
            self.p_cards.append(temp)
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
            self.d_cards.append(temp)
            temp = temp.split()
            if temp[1] in ['J','Q', 'K']:
                self.d_value += 10
            elif temp[1] == 'Ace':
                if (self.d_value + 11 <= 21):
                    self.d_value += 11
                else:
                    self.d_value += 1 
            else:
                self.d_value += int(temp[1])
            print ' The Accumulated hand of the House is %i' %self.d_value
            
        
    def Check_win(self):
        '''
        method that checks:
            If the player or the house has 21
            If the player or the house is busted
            Who won in previous cases, plus in the case Player and House stand
            [the winner is the one with higher hand without exceeding 21]
        '''
        if self.p_value > 21:
            print ' Player %s Busted!  House wins\n' %self.player
            return 'H'
        elif self.d_value > 21:
            print ' Player %s wins!  House busted\n' %self.player
            # money equal to 3:2 of the Bet will be returned to the player
            return 'P'
        elif self.p_value == 21 and self.d_value != 21:
            print ' Player %s wins  21 achieved!!\n' %self.player
            # money equal to 3:2 of the Bet will be returned to the player
            return 'P'
        elif self.d_value == 21 and self.p_value !=21:
            print ' The House wins the game, 21 achieved\n' 
            # The player looses the bet
            return 'H'
        elif self.p_value == 21 and self.d_value == 21:
            print ' The game ends in a Tie\n'
            #money equal to the player bet is returned to the player
            return 'T'
        elif self.p_hit == False and self.d_hit == False:
            if self.p_value > self.d_value:
                print ' Player %s wins  higher value than the House!!\n' %self.player
                return 'P'
            elif self.p_value == self.d_value:
                print ' The game ends in a Tie\n'
                #money equal to the player bet is returned to the player
                return 'T'
            else:   
                print ' The House wins the game, Higher value than the player\n'
                return 'H'
        else:
            return None
    

