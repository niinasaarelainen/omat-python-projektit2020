
class Cart:

    def __init__(self, x, y, symboli):
        self.x = x
        self.y = y
        self.symbolit = ["^", ">", "v", "<"]
        self.symboli = symboli
        self.directions = [0, 1, 2, 3] # ylös, oik, alas, vas 
        self.direction = self.directions[self.symbolit.index(self.symboli)]
        self.kaantosuunnat = [-1, 0, 1]    # left, straight, right
        self.kaanto_nro = 2
        self.kaantosuunta = self.kaantosuunnat[self.kaanto_nro]
        
        
    def next_direction(self):
        self.kaanto_nro += 1
        self.kaanto_nro = self.kaanto_nro % 3
        self.kaantosuunta = self.kaantosuunnat[self.kaanto_nro]
        self.direction = (self.direction + self.kaantosuunta) % 4
        self.symboli = self.symbolit[self.direction]

    def turn(self, suunta):
        self.direction = (self.direction + suunta)  % 4
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

