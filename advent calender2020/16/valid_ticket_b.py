
data = []
ranget = {}  
tickets = []  
tickets_sarakkeet = []  
tickets_sarakkeet_hash = {}
your_ticket = {11 : "" , 12 : "" , 13 : "" }  # "" tulee rangen nimi myöhemmin
#your_ticket = [107,157,197,181,71,113,179,109,97,163,73,53,101,193,173,151,167,191,127,103]
              #  0      2       4       6      8      10     12     14  

def readfile():  
    f = open("data_ranget.txt", "r")  

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

    f = open("data_tickets.txt", "r")  

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
        tickets_sarakkeet_hash[str(s)] = []
    
    print(tickets_sarakkeet_hash)

"""
def onkoRangella():
    validit_luvut = []  

    for t in tickets_sarakkeet:
        for luku in t:
            for min, max in ranget.values():
                if luku >= min and luku <= max:
                    #print(luku, "on välillä", min, max)
                    validit_luvut.append(luku) 
                    break

    epävalidit = [t for t in tickets for luku in t if luku not in validit_luvut]
    validit = [t for t in tickets if t not in epävalidit]
    return validit  """


def positions():
    for sarake_ind in range(len(tickets_sarakkeet)):   
        for luku in tickets_sarakkeet[sarake_ind]:
            for nimi, values in ranget.items():
                min0, max0 = values[0]
                min1, max1 = values[1]
                if (luku >= min0 and luku <= max0) or (luku >= min1 and luku <= max1):
                    pass
                else:
                    print(luku, min0, max0, min1, max1)
                    if sarake_ind not in ranget[nimi][-1]:
                        ranget[nimi][-1].append(sarake_ind)
                    

"""
def loytyyko_rangeista():
    #print(len(tickets_sarakkeet))    # 20 kpl, sama määrä kuin ranget
    for nimi, v in ranget.items():
        for sarake in tickets_sarakkeet:
            #print(len(set(v[-1]) & set(sarake)), len(ranget))
            if len(set(v[-1]) & set(sarake)) >= len(ranget):                              # set ja &   !!!!!!!
                print(set(v[-1]), set(v[-1]) & set(sarake))
                tickets_sarakkeet_hash[str(sarake)].append(nimi) 
    

def tutki_hashit():
    s = sorted(tickets_sarakkeet_hash.items(), key=lambda item: len(item[1]))
    vastaukset = []
    vastausJarjestys = []
    for sarake, nimilista in s:
        print(tickets_sarakkeet_hash[sarake])   
        for nimi in nimilista:         
            if nimi not in vastaukset:
                vastausJarjestys.append(nimi)
                vastaukset.append(nimi)

    print(vastausJarjestys)    """
                        


readfile()
muodosta_tickets_sarakkeet()
muodosta_tickets_sarakkeet_hash()
positions()
print(ranget.items())
s = sorted(ranget.items(), key=lambda item: len(item[1][2]))
print(s)
print()
for nro in range(len(s)):
    for data in s[nro]:
        
            print(data[-1])     # 661094006513  too low
                              # 1070018134253  too low