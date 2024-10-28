data = []
ranget = []   # [['1', '3'], ['5', '7'], ['6', '11'], ['33', '44'], ['13', '40'], ['45', '50']]
tickets = []   # ['7', '3', '47', '40', '4', '50', '55', '2', '20', '38', '6', '12']


def readfile():  
    f = open("data_ranget.txt", "r")  

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

    f = open("data_tickets.txt", "r")  

    for rivi in f:
        sp = rivi.strip().split(",")
        for luku in sp:
            tickets.append(int(luku))

    print(tickets)
                    


def onkoRangella():
    validit = []  

    for luku in tickets:
        for min, max in ranget:
            if luku >= min and luku <= max:
                print(luku, "on välillä", min, max)
                validit.append(luku) 
                break
    print(validit)

    epävalidit = [luku for luku in tickets if luku not in validit]
    return epävalidit


readfile()
print(sum(onkoRangella()))