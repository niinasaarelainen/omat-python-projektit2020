import math

data = []
koodi = {"A":"A", "K":"B", "Q":"C", "T":"E", "9":"F", "8":"G", "7":"H", "6":"I", "5":"J", "4":"K", "3":"L", "2":"M", "J":"N" }
hands = {}   
rankings = {}
samoja_lkm = {}
samoja_cards = {}
rankings_tulos = {}
#hand = "T55J5"

def readfile():   
    f = open("data_1.txt", "r")         
    for rivi in f:
        sp = rivi.strip().split(" ")
        koodattu_kasi = koodaa(sp[0])
        hands[koodattu_kasi] = int(sp[1])

def koodaa(hand):
    k = ""
    for card in hand:
        k += koodi[card]
    return k


def rank(hand):
    global samoja_lkm, samoja_cards
    samoja_lkm = {}
    samoja_cards = {}
    jokerit = 0

    for card in hand:
        if card == "N": 
            jokerit += 1
            continue
            
        if card not in samoja_cards:  # tänne ei jokereita
            samoja_cards[card] = [card]
        else:
            samoja_cards[card].append(card)

        if card not in samoja_lkm:   # eikä tänne
            samoja_lkm[card] = 1
        else:
            samoja_lkm[card] += 1

    montako = [v for v in samoja_lkm.values()]
    
    #print(montako)
    if jokerit == 5:
        montako.append(5)
    else:
        isoin = max(montako)
        montako.remove(isoin)
        montako.append(isoin + jokerit)

    if hand == "NNNNG":
        print("NNNNG", montako)


    #alustava ranking, ei ota kantaa samojen käsien väliseen paremm.
    if 5 in montako:
        rank = 1
    elif 4 in montako:
        rank = 2
    elif 3 in montako and 2 in montako: # täyskäsi
        rank = 3
        print(hand)
    elif 3 in montako:
        rank = 4
    elif 2 in montako:  # 2 paria
        montako.remove(2)
        if 2 in montako:
            rank = 5
        else:
            rank = 6
    else:
        rank = 7

    if rank not in rankings:
        rankings[rank] = [hand]
    else:
        rankings[rank].append(hand)

    #samoja_cards_all.append(samoja_cards)



def samat_kadet():
    #print(rankings)

    for rank in rankings:
        if len(rankings[rank]) > 1:
            rankings[rank] = sorted(rankings[rank])
            
    s = sorted(rankings.items(), key=lambda x: x[0])
    #print(s)
    the_lista = []
    for item in s:
        #print("item", item)
        the_lista += item[1]

    rank = len(the_lista)
    for item in the_lista:
        rankings_tulos[item] = rank
        rank -= 1


readfile()
for hand in hands:
    rank(hand)
#print(hands) 

"""
koodattu_kasi = koodaa(hand)
print(koodattu_kasi)     # EJJDJ    D = jokeri
rank(koodattu_kasi) """

#print("\nrankings", rankings)
#print("samoja_cards_all", samoja_cards_all)
samat_kadet()
#print("\nrankings_tulos", rankings_tulos)

tulot = []
for hand in hands:
    tulot.append(hands[hand] * rankings_tulos[hand])
print(sum(tulot))  # 254223992   too low
                   # 251548123, 253946228, 254355560
                   # 255632664