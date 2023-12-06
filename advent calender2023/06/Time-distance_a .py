from functools import reduce


data = []
times = []
dists= []
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
        print(self.traveled)

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
        if ind== 0:
            sp = data[ind].split(" ")
            for time in sp:
                if time != "":
                    times.append(int(time))
        else:
            sp = data[ind].split(" ")
            for dist in sp:
                if dist != "":
                    dists.append(int(dist))

        

readfile()
tutki()
print(times, dists)

for i in range(len(times)):
    k = Race(times[i], dists[i])    
    k.etsiMax()
    k.waysToWin()
    ways_to_win.append(k.ways_to_win)
    print(ways_to_win)

mul = reduce((lambda x, y: x * y), ways_to_win)
print(mul)