#!/usr/bin/python

import random
import numpy as np
import time
import graphics as gp



decks = np.ndarray(shape=(8,13))

def shuffle():
    for i in range(0,8):
        for j in range(0,13):
            if j<10:
                decks[i][j] = j+1  #setting values of cards
            else:
                decks[i][j] = 10
def getCard():
    while True:
        suit = random.randint(0,7)
        card = random.randint(0,12)

        if decks[suit][card] == 0:
            continue

        else:
            return (suit,card)

def aceCheck(card):
    if card == 0:
        return True
    else:
        return False

def dealer2(d1):
        d2 = PlayerCard()
        print
        sum = d1.value + d2.value
        ace = 0
        if d1.ace == True:
            sum = sum + 10
            ace += 1
        if d2.ace == True:
            sum = sum + 10
            ace += 1
        print "Dealer's cards are ",d1.face,"of ",d1.suit,"and ",d2.face,"of ",d2.suit,".\n"
        print "Value of ",sum,".\n"
        if sum == 21:
            print "Blackjack!"
            time.sleep(3)
            return sum
        while sum <17:
            time.sleep(3)
            ap = PlayerCard()
            sum = sum + ap.value
            if ap.ace == True:
                sum = sum +10
                ace += 1
            print "Next card is ",ap.face,"of ",ap.suit,"."
            if (ap.ace == True or ace>0)and sum>21:
                while sum>21 and ace>0:
                    sum = sum-10
                    ace -=1
            print "Value of: ",sum,"\n"

            if sum == 21:
                print "Uh oh"
                time.sleep(1)
                return sum
            if sum > 21:
                print "Busted"
                return 1/2

        return sum

def playGame(list,players):
    i = 0
    d1 = PlayerCard()
    while i < players:
        ace = 0
        print "\n\nDealer shows a",d1.face,"of",d1.suit,"\n"
        time.sleep(2)
        print "\n\nPlayer",i+1,":"
        ap1 = PlayerCard()
        ap2 = PlayerCard()
        sum = ap1.value + ap2.value

        if ap1.ace == True:
            sum = sum + 10
            ace += 1
        if ap2.ace == True:
            sum = sum + 10
            ace += 1
        print "Your Cards are ",ap1.face,"of ",ap1.suit,"and ",ap2.face,"of ",ap2.suit,".\n"
        if sum == 21:
            print "Congrats, you got Blackjack!"
            time.sleep(3)
            list[i] == "22"
            i+=1 #increment player
            continue
        print "Value of ",sum,".\n"
        while True:
            print "Would you like to Hit or Stand??"
            answer = raw_input()
            if answer == "Hit" or answer == "hit":
                ap = PlayerCard()
                sum = sum + ap.value
                if ap.ace == True:
                    sum = sum +10
                    ace += 1
                print "Your card is ",ap.face,"of ",ap.suit,"."
                if (ap.ace == True or ace>0)and sum>21:
                    while sum>21 and ace>0:
                        sum = sum-10
                        ace -=1
                if sum == 21:
                    print "21!"
                    time.sleep(3)
                    list[i] = sum
                    i+=1
                    break
                if sum > 21:
                    print "Busted"
                    time.sleep(3)
                    list[i] = 0
                    i+=1
                    break
                print "\nTotal Value: ",sum,"."
                continue
            if answer == "Stand" or answer == "stand":
                list[i] = sum
                i+=1
                break

    dealer = dealer2(d1)
    checkWinners(list,dealer)

class PlayerCard():

    def __init__(self):
        suit,card = getCard()
        self.makeCard(suit,card)
        self.ace = aceCheck(card)
        self.value = decks[suit][card]
        decks[suit][card] = 0

    def makeCard(self,suit,card):
        if (suit+1) % 4 == 1:
            self.suit = "Hearts"

        elif (suit+1) % 4 == 2:
            self.suit = "Spades"

        elif (suit+1) % 4 == 3:
            self.suit = "Clubs"

        elif (suit+1) % 4 == 0:
            self.suit = "Diamonds"

        if (card) == 10:
            self.face = "Jack"

        elif (card) == 11:
            self.face = "Queen"

        elif (card) == 12:
            self.face = "King"

        elif (card) == 0:
            self.face = "Ace"

        if card < 10 and card > 0:
            self.face = card + 1


def checkWinners(list,dealer):
    for x in range(len(list)):
        time.sleep(2)
        if list[x]>dealer:
            print "Player",x+1,"Won\n"
        elif list[x]<dealer:
            print "Player",x+1,"Lost\n"
        elif list[x]==dealer:
            print "Player",x+1,"Pushed\n"

if __name__ == "__main__":
    shuffle()
    count = 0
    while True:
        count+=1
        print "How many players want to play? "
        if count == 8:
            shuffle()
        players = input()
        list = [0]*players
        playGame(list,players)

            #while True:
            #    print "1)Hit\n2)Stand\n\n"
            #    choice = input()
            #    if choice == 1:
            #        hit = PlayerCard()
            #        list[i] = list[i] + hit.value
            #        if list[i] > 21:
            #            print "You lose"
            #            break
            #        else:
            #            continue
            #    else:
            #        break
