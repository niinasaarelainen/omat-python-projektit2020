data = []
ranget = {}  
tickets = []  
tickets_sarakkeet = []  
tickets_sarakkeet_hash = {}
your_ticket = {11 : "" , 12 : "" , 13 : "" }  # "" tulee rangen nimi myöhemmin
#your_ticket = [107,157,197,181,71,113,179,109,97,163,73,53,101,193,173,151,167,191,127,103]


def readfile():  
    f = open("data_b_ranget.txt", "r")  

    for rivi in f:
        nimi, rivi = rivi.split(":")
        sp = rivi.strip().replace(" or", "").split(" ")
        for osa in sp:
            if ":" not in osa:
                min, max = osa.split("-")
                if nimi not in ranget:
                    ranget[nimi] = [[int(min), int(max)]]
                else:
                    ranget[nimi].append([int(min), int(max)])
        ranget[nimi].append([])

    print(ranget)

    f = open("data_b_tickets.txt", "r")  

    for rivi in f:
        sp = rivi.strip().split(",")
        ticket = []
        for luku in sp:
            ticket.append(int(luku))
        tickets.append(ticket)    


def muodosta_tickets_sarakkeet():       
    for ind in range(len(ranget)):
        tickets_sarakkeet.append([])
        for t in tickets:
            tickets_sarakkeet[-1].append(t[ind])       
    #print(tickets_sarakkeet)                            #  [3, 15, 5], [9, 1, 14], [18, 5, 9]

def muodosta_tickets_sarakkeet_hash():
    for s in tickets_sarakkeet:
        print(" s", s)
        tickets_sarakkeet_hash[str(s)] = []
    
    print(tickets_sarakkeet_hash)


def onkoRangella():
    validit_luvut = []  

    for t in tickets:
        for luku in t:
            for min, max in ranget.values():
                if luku >= min and luku <= max:
                    #print(luku, "on välillä", min, max)
                    validit_luvut.append(luku) 
                    break

    epävalidit = [t for t in tickets for luku in t if luku not in validit_luvut]
    validit = [t for t in tickets if t not in epävalidit]
    return validit


def positions():
    ind = 1
    for t in tickets:   # [3, 9, 18]
        for luku in t:
            for nimi, values in ranget.items():
                
                for i in range(0, 2):
                    min, max = values[i]
                    if luku >= min and luku <= max:
                        ranget[nimi][-1].append(luku)

def loytyyko_rangeista():
    for nimi, v in ranget.items():
        for sarake in tickets_sarakkeet:
            if len(set(v[-1]) & set(sarake)) == len(ranget):                              # set ja &   !!!!!!!
                tickets_sarakkeet_hash[str(sarake)].append(nimi)


def tutki_hashit():
    s =sorted(tickets_sarakkeet_hash, key=lambda h: len(tickets_sarakkeet_hash[h]))
    print(tickets_sarakkeet_hash)

    #s = sorted(tulokset, key=lambda tulos: (-tulos.topit_lkm, tulos.topit_yritykset, -tulos.zonet_lkm, tulos.zonet_yritykset))  
      
        
                        


readfile()
muodosta_tickets_sarakkeet()
muodosta_tickets_sarakkeet_hash()
positions()
print(ranget)
loytyyko_rangeista()
tutki_hashit()