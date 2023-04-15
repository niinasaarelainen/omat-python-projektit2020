
data = []  
all_discs = []   # huom  Disc #1 indeksissä 0


class Disc():
    
    def __init__(self, id, pos_amount, pos_start) :
        self.id = id   # tämä kertoo myös kauanko kestää alkuhetkeen
        self.pos_amount = pos_amount
        self.pos = (pos_start + self.id) % self.pos_amount

    def next(self):
        self.pos = (self.pos + 1) % self.pos_amount
        


def readfile():
    f = open( "data_b.txt", "r") 
    for rivi in f:
        rivi = rivi.strip()
        data.append(rivi.split(" "))

def lue():
    monesko_disc = 1
    for rivi in data:
        all_discs.append(Disc(monesko_disc, int(rivi[3]), int(rivi[11][0])))
        monesko_disc += 1

def positions():
    for d in all_discs:
        #print(d.pos, end="")
        if d.pos != 0:
            #print()
            return False
    
    return True
            

def next():
    for d in all_discs:
        d.next()

readfile()
lue()
positions()
for i in range(5655555):
    next()
    if positions():
        print("vastaus: ", i + 1)
        break
