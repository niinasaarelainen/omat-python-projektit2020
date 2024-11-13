
pakka1 = [9,2,6,3,1]
pakka2 = [5,8,4,7,10]
#pakka1 = []
#pakka2 = []


def readfile():      
    f = open("data.txt", "r")     
    eka = True    
    for rivi in f:
        if rivi.strip() == '':
            eka = False
        elif eka:
            pakka1.append(int(rivi.strip()))
        else:
            pakka2.append(int(rivi.strip()))
    print(pakka1, pakka2)

"""Before either player deals a card, if there was a previous round in this game that had 
exactly the same cards in the same order in the same players' decks, the game instantly 
ends in a win for player 1. Previous rounds from other games are not considered. 
(This prevents infinite games of Recursive Combat, which everyone agrees is a bad idea.)

Otherwise, this round's cards must be in a new configuration; the players begin the round by 
each drawing the top card of their deck as normal.

If both players have at least as many cards remaining in their deck as the value of the card 
they just drew, the winner of the round is determined by playing a new game of Recursive Combat .

Otherwise, at least one player must not have enough cards left in their deck to recurse; 
the winner of the round is the player with the higher-value card."""


def play():
    while pakka2 != [] and pakka1 != []:
        p1 = pakka1.pop(0)
        p2 = pakka2.pop(0)
        if p1 > p2:
            pakka1.append(p1)
            pakka1.append(p2)
        else:
            pakka2.append(p2)
            pakka2.append(p1)
        print(p1, p2, pakka1, pakka2)


def score():
    kerroin = 1
    tulos = 0

    voittopakka = max(sorted([pakka1, pakka2], key = lambda x: len(x)))

    for card in reversed(voittopakka):
        tulos += kerroin * card
        kerroin += 1
    print(tulos)

#readfile()
play()
score()