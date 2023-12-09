import math

data = []
koodi = {"A":"A", "K":"B", "Q":"C", "J":"D", "T":"E", "9":"F", "8":"G", "7":"H", "6":"I", "5":"J", "4":"K", "3":"L", "2":"M" }
hands = {}   # aluksi: 32T3K = 765
rankings = {}
samoja_lkm = {}
samoja_cards = {}
rankings_tulos = {}

def readfile():   
    f = open("data.txt", "r")         
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
    global samoja_lkm
    samoja_lkm = {}

    for card in hand:

        if card not in samoja_lkm:
            samoja_lkm[card] = 1
        else:
            samoja_lkm[card] += 1

    montako = [v for v in samoja_lkm.values()]
    print(hand, montako)
    

    #alustava ranking, ei ota kantaa samojen käsien väliseen paremm.
    if 5 in montako:
        rank = 1
    elif 4 in montako:
        rank = 2
    elif 3 in montako and 2 in montako: # täyskäsi
        rank = 3
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


def samat_kadet():
    print(rankings)

    for rank in rankings:
        if len(rankings[rank]) > 1:
            rankings[rank] = sorted(rankings[rank])
            
    s = sorted(rankings.items(), key=lambda x: x[0])
    #print(s)
    the_lista = []
    for item in s:
        print("item", item)
        the_lista += item[1]

    rank = len(the_lista)
    for item in the_lista:
        rankings_tulos[item] = rank
        rank -= 1


readfile()
for hand in hands:
    rank(hand)
print(hands)

print("\nrankings", rankings)
samat_kadet()
print("\nrankings_tulos", rankings_tulos)

tulot = []
for hand in hands:
    tulot.append(hands[hand] * rankings_tulos[hand])
print(sum(tulot))   # 251927063