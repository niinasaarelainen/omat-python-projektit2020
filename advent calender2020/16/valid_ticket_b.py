data = []
ranget = []   # [['1', '3'], ['5', '7'], ['6', '11'], ['33', '44'], ['13', '40'], ['45', '50']]
tickets = []   # ['7', '3', '47', '40', '4', '50', '55', '2', '20', '38', '6', '12']
your_ticket = [107,157,197,181,71,113,179,109,97,163,73,53,101,193,173,151,167,191,127,103]


def readfile():  
    f = open("data_1_ranget.txt", "r")  

    for rivi in f:
        ind = rivi.find(":")
        print(ind)
        rivi = rivi[ind:]
        sp = rivi.strip().replace(" or", "").split(" ")
        for osa in sp:
            if ":" not in osa:
                min, max = osa.split("-")
                ranget.append([int(min), int(max)])

    print(ranget)

    f = open("data_1_tickets.txt", "r")  

    for rivi in f:
        sp = rivi.strip().split(",")
        ticket = []
        for luku in sp:
            ticket.append(int(luku))
        tickets.append(ticket)

    print(tickets)
                    


def onkoRangella():
    validit = []  

    for t in tickets:
        for luku in t:
            for min, max in ranget:
                if luku >= min and luku <= max:
                    print(luku, "on välillä", min, max)
                    validit.append(luku) 
                    break
        print("validit", validit)

        epävalidit = [luku for luku in tickets if luku not in validit]
        return epävalidit


readfile()
print(onkoRangella())