data = []
esteet = []
guard_x = -1
guard_y = -1

class Guard:

    def __init__(self, y, x, esteet) -> None:
        self.x = x
        self.y = y
        self.suunta_x = 0   # eka suunta
        self.suunta_y = 3   # vika suunta
        self.esteet = esteet
        self.traveled = []     # tänne olisi pitänyt laittaa lähtötilanne, oikea vastaus koska listaan tuli myös 1. ulkona
        self.suunnat = [0, 1, 0, -1]

    def seuraavaSuunta(self):        
        self.suunta_x = (self.suunta_x + 1) % 4
        self.x += self.suunnat[self.suunta_x]
        self.suunta_y = (self.suunta_y + 1) % 4
        self.y += self.suunnat[self.suunta_y]
        

    def travel(self):
        self.x += self.suunnat[self.suunta_x]
        self.y += self.suunnat[self.suunta_y]
        if [self.y, self.x] in self.esteet:
            # ei mennäkkään:
            self.x -= self.suunnat[self.suunta_x]
            self.y -= self.suunnat[self.suunta_y]
            self.seuraavaSuunta()
        if [self.y, self.x] not in self.traveled:
            self.traveled.append([self.y, self.x])

####  END  CLASS  Guard   ##############


def readfile():   
    f = open("data.txt", "r")         
    for rivi in f:
        data.append(rivi.strip())

def tutki():
    global guard_x, guard_y
    for y in range(len(data)):        
        l = list(data[y])
        for x in range(len(data[y])):
            if data[y][x] == "#":
                esteet.append([y,x])
            elif data[y][x] == "^":
                guard_x = x
                guard_y = y
        

readfile()
tutki()
#print(esteet, guard_y, guard_x)
g = Guard(guard_y, guard_x, esteet)

while g.x >= 0 and g.x < len(data) and g.y >= 0 and g.y < len(data):
    g.travel()

print(g.traveled)
print(len(g.traveled))

