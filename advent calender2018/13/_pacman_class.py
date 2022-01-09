
class Pacman:

    def __init__(self, x, y, symboli):
        self.x = x
        self.y = y
        self.x_wanha = x  
        self.y_wanha = y 
        self.symbolit = ["^", ">", "v", "<"]
        self.symboli = symboli
        self.directions = [0, 1, 2, 3] # ylös, oik, alas, vas 
        self.direction = self.directions[self.symbolit.index(self.symboli)]
        if symboli == "^":
            self.vari = (233, 3, 3)
        if symboli == ">":
            self.vari = (3, 233, 3)
        
        
    def next_direction(self, pac_kaantymispyynto):
        self.direction = pac_kaantymispyynto
        self.symboli = self.symbolit[self.direction]

    def turn(self, suunta):
        self.direction = (self.direction + suunta)  % 4
        self.symboli = self.symbolit[self.direction]

    def liiku(self):

        self.y_wanha = self.y
        self.x_wanha = self.x

        if self.direction == 0:
            self.y -= 1            
        if self.direction == 2:
            self.y += 1            
        if self.direction == 1:
            self.x += 1            
        if self.direction == 3:
            self.x -= 1
        
       
