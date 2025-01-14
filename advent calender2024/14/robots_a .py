data = []
sijainnit = []
x = 2
y = 4 
suunta_x = 2
suunta_y = -3
kuva = []
width = 11
height = 7
robotit = []

class Robot:

    def __init__(self, x, y, suunta_x, suunta_y) -> None:
        self.x = x
        self.y = y
        self.suunta_x = suunta_x
        self.suunta_y = suunta_y
        kuva[self.y][self.x] += 1
        self.traveled = []     # tänne olisi pitänyt laittaa lähtötilanne, oikea vastaus koska listaan tuli myös 1. ulkona
      

    def travel(self):
        kuva[self.y][self.x] -= 1
        self.x += self.suunta_x
        self.x = self.x % width
        self.y += self.suunta_y
        self.y = self.y % height
        print(self.y, self.x)
        kuva[self.y][self.x] += 1

####  END  CLASS  Robot   ##############


def readfile():   
    f = open("data_1.txt", "r")         
    for rivi in f:
        data.append(rivi.strip())

def muodostaSijainnit():
    global x, y, suunta_x, suunta_y
    for rivi in data:
        sij, suunta = rivi.split(" ")

        xx, yy = sij.split("=")[1].split(",")
        x = int(xx)
        y = int(yy)

        xs, ys = suunta.split("=")[1].split(",")
        suunta_x = int(xs)
        suunta_y = int(ys)

        robotit.append(Robot(x, y, suunta_x, suunta_y))

def alustaMatriisi():
    for y in range(height):
        rivi = []
        for x in range(width):
            rivi.append(0)
        kuva.append(rivi) 

def printtaa():
    for y in range(height):
        for x in range(width):
            print(kuva[y][x], end= "")
        print()
    print()
            

def quadrant():

    quad1 = 0
    quad2 = 0
    quad3 = 0
    quad4 = 0
    
    semi_x = width // 2
    semi_y = height // 2

    #1
    for y in range(semi_y):
        quad1 += sum(kuva[y][:semi_x])
    print(quad1)

    #2
    for y in range(semi_y):
        print(kuva[y + semi_y + 1][:semi_x])
        quad2 += sum(kuva[y + semi_y + 1][:semi_x])
    print(quad2)

    #3
    for y in range(semi_y):
        #print(kuva[y][semi_x + 1:])
        quad3 += sum(kuva[y][semi_x + 1:])
    print(quad3)

    #4
    for y in range(semi_y):
        print(kuva[y + semi_y + 1][semi_x + 1:])
        quad4 += sum(kuva[y + semi_y +1][semi_x + 1:])
    print(quad4)

    return (quad1*quad2*quad3*quad4)



   


        

readfile()
alustaMatriisi()
muodostaSijainnit()
printtaa()

for i in range(100):
    for r in robotit:
        r.travel()
    
printtaa()
vastaus = quadrant()
print(vastaus)



