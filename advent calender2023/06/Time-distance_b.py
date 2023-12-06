from functools import reduce


data = []
time = 0
dist= 0
kilpailut = []
ways_to_win = []


class Race:

    def __init__(self, time, dist) -> None:
        self.time = time
        self.dist_record = dist
        self.current_dist = 0
        self.traveled = []
        self.ways_to_win = 0

    def etsiMax(self):
        for hold_button in range(self.time):
            kulje = self.time - hold_button
            self.traveled.append(hold_button * kulje)

    def waysToWin(self):
        self.ways_to_win = len([tulos for tulos in self.traveled if tulos > self.dist_record])


####  END  CLASS  RACE   ##############

def readfile():   
    f = open("data.txt", "r")         
    for rivi in f:
        sp = rivi.split(":")
        data.append(sp[1].strip())

def tutki():
    global time, dist
    for ind in range(len(data)):
        kokoa_luku = ""
        if ind== 0:
            for merkki in data[ind]:
                if merkki != " ":
                    kokoa_luku += merkki
            time = int(kokoa_luku)
        else:
            for merkki in data[ind]:
                if merkki != " ":
                    kokoa_luku += merkki
            dist = int(kokoa_luku)
        

readfile()
tutki()
print(time, dist)

k = Race(time, dist)    
k.etsiMax()
k.waysToWin()
ways_to_win.append(k.ways_to_win)
print(ways_to_win)

mul = reduce((lambda x, y: x * y), ways_to_win)
print(mul)