# -*- coding: utf-8 -*-
"""
Created on Sat May 20 12:20:39 2017
This script is the handler for BlackJAck Games. It uses the classess defined
in blackjackclass.py
@author: iibanez
"""
from blackjackclass import *

print ' Welcome to the Black Jack Simulator\n'
print '\n\n\n'
print 'First, we will define the Player Data, consisting in his/her name and initial credit\n\n'
while True:
    try:
        p_name = str(raw_input('Please, Introduce the name of the player  '))
        break
    except:
        print 'That is not a valid option, please introduce a valid name'
    
while True:
    try:
        bankroll = int(raw_input('Please, Introduce the initial credit of the player  '))
        break
    except:
        print 'That is not a valid option, please introduce an Integer'
playerA = player(p_name, bankroll)
print '\n'
print 'Player succesfully created:\n'
print 'Player name             %s\n' %playerA.p_name
print 'Player initial credit   %i\n' %playerA.bankroll

            
while playerA.bankrupcy == False:
    while True:
        try:
            print ' %s Do you want to start a new game?\n' %playerA.p_name
            answer = raw_input('Please answer Y/N:' ).upper()
            if answer == 'Y' or answer == 'N':
                break
            else:
                raise
        except:
            print " Sorry, that's not a valid answer, please answer Y/N"
    if answer == 'N':
        print 'Thank you for playing to Black jack. See you soon!\n'
        print 'final stats of the leaving player\n\n'
        print 'Player name             %s\n' %playerA.p_name
        print 'Player final credit   %i\n' %playerA.bankroll
        break
    else:
        while True:
            try:
                print ' %s ,how much do you want to bet? you have %i funds\n' %(playerA.p_name, playerA.bankroll)
                bet = int(raw_input(':  ' ))
                if bet <= playerA.bankroll:
                    break
                else:
                    raise
            except:
                    print ' Sorry, answer not valid, must be an integer number of Bitcoins'
                    print ' You need to have enough funds to bet'
        juego =game(playerA.p_name, bet)
        playerA.substract_bankroll(juego.p_bet)
        print 'Initial round, %s and the House take two cards\n' %juego.player
        juego.take_card('P')
        juego.take_card('P')
        juego.take_card('H')
        juego.take_card('H')
        winner = juego.Check_win()
        if winner == 'P':
            prize = (juego.p_bet * 3)/2
            print ' %s  has won %i bitcoins!!!\n' %(juego.player , prize)
            playerA.add_bankroll(prize)
        elif winner == 'H':
            print '  %s  has lost %i bitcoins!!!\n' %(juego.player , juego.p_bet)
        elif winner == 'T':
            print ' The win ends in a Tie, game bets are returned'
            playerA.add_bankroll(juego.p_bet)
        while winner is None:    
            while True:
                try:
                    if juego.p_hit == True:
                        print 'Next Round'
                        juego.show_cards()
                        print ' The Accumulated value for %s is %i\n\n' %(juego.player, juego.p_value)
                        print '%s Do you want to Hit or Stand?\n' %juego.player
                        answer = raw_input('Please answer H/S:' ).upper()
                        if answer == 'H' or answer == 'S':
                            break
                        else:
                            raise
                    else:
                        answer ='House_only'
                        break
                except:
                    print " Sorry, that's not a valid answer, please answer H for Hit and S for Stand"
            if answer == 'S':
                juego.p_hit = False
                if juego.d_value <= 17:
                    juego.take_card('H')
                    juego.show_cards()
                    print ' The House value is %i\n' %juego.d_value
                else:
                    juego.d_hit = False
            elif answer == 'H':
                juego.take_card('P')
                if juego.d_value <= 17:
                    juego.take_card('H')
                    juego.show_cards()
                    print ' The House value is %i\n' %juego.d_value
                else:
                    juego.d_hit = False
            elif answer == 'House_only':
                if juego.d_value <= 17:
                    juego.take_card('H')
                    juego.show_cards()
                    print ' The House value is %i\n' %juego.d_value
                else:
                    juego.d_hit = False
            winner = juego.Check_win()
            if winner == 'P':
                prize = (juego.p_bet * 3)/2
                print ' %s  has won %i bitcoins!!!\n' %(juego.player , prize)
                playerA.add_bankroll(prize)
            elif winner == 'H':
                print '  %s  has lost %i bitcoins!!!\n' %(juego.player , juego.p_bet)
            elif winner == 'T':
                print ' The win ends in a Tie, game bets are returned'
                playerA.add_bankroll(juego.p_bet)
            if playerA.bankrupcy == True:
                print ' The player has not enough funds, Do you want to add more Funds?'
                while True:
                    try:
                        amount = int(raw_input('Please, Introduce additional credit or 0 for denial  '))
                        check =isinstance(amount, ( int, long))
                        if check == True:
                            break
                        else:
                            raise
                    except:
                        print 'That is not a valid option, please introduce an Integer'
                playerA.get_credit(amount)
print 'Thank you for playing to Black jack. See you soon!\n'
print 'final stats of the leaving player\n\n'
print 'Player name             %s\n' %playerA.p_name
print 'Player final credit   %i\n' %playerA.bankroll                
