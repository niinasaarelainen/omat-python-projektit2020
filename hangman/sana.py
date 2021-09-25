import random

class Sana:

    def __init__(self):
        self.sanat = []
        self.valittusana = ""


    def sanalista(self):
        f = open("sanat.txt", "r")
        for sana in f:
            self.sanat.append(sana.strip().replace("Ã¤", "ä").replace("Ã¶", "ö"))
        print(len(self.sanat))   


    def valitsesana(self):
        r = random.randint(0, len(self.sanat)-1)
        self.valittusana = self.sanat[r]
        print(self.valittusana )
        