
class Cart:

    def __init__(self, x, y, myota):
        self.x = x
        self.y = y
        self.myota = myota
        self.directions = [0, 1, 2, 3] # ylös, oik, alas, vas 
        self.direction = self.directions[self.myota]
        self.kaantosuunnat = [-1, 0, 1]    # left, straight, right
        self.kaanto_nro = 2
        self.kaantosuunta = self.kaantosuunnat[self.kaanto_nro]
        self.symbolit = ["^", ">", "v", "<"]
        self.symboli = self.symbolit[self.direction]
        
    def next_direction(self):
        self.kaanto_nro += 1
        self.kaanto_nro = self.kaanto_nro % 3
        self.kaantosuunta = self.kaantosuunnat[self.kaanto_nro]
        self.direction = self.direction + self.kaantosuunta
        self.symboli = self.symbolit[self.direction]

    def turn(self):
        self.direction = (self.direction + self.myota)  % 4
        self.symboli = self.symbolit[self.direction]



    def liiku(self):
        if self.direction == 0:
            self.y -= 1
        if self.direction == 2:
            self.y += 1
        if self.direction == 1:
            self.x += 1
        if self.direction == 3:
            self.x -= 1

