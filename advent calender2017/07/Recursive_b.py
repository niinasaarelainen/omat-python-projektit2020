
class Solu:
    def __init__(self, nimi, paino):
        self.nimi = nimi        
        self.paino = paino
        self.lapset = []

    def lapseta(self, lapset):
        self.lapset = lapset


data_lapset = []
data_all = []
dic = {}
solut = []



def readfile():
    f = open("data_a.txt", "r") 
    for rivi in f:
        rivi = rivi.strip()
        if "->" in rivi:
            data_lapset.append(rivi.split("->"))
        data_all.append(rivi)


def teeDic():
    for rivi in data_lapset:
        dic[rivi[0].split(" ")[0]] = rivi[1].replace(",", "").split(" ")

    #print(dic)


def muodostaLuokat():
    for rivi in data_all:
        nimi, paino = rivi.split("(")
        paino, loput = paino.split(")")
        solut.append(Solu(nimi.replace(" ", ""), paino.replace(")", "")))

    nimet = [s.nimi for s in solut]
    print(nimet)
    painot = [s.paino for s in solut]
    print(painot)

def lapseta():
    for item in dic:
        [s.lapseta(dic[item]) for s in solut if s.nimi == item]
        
    lapset = [s.lapset for s in solut]    
    print(lapset)

def laskePaino():
    yhteispaino = 0

    kutsuMua("tknk")

    def kutsuMua(nimi):
        for s in solut:
            if  nimi in s.nimi:
                lapset = s.lapset 
        print(lapset)
        for lapsi in lapset:        
            if lapsi != "":
                for s in solut:
                    if  lapsi in s.nimi:
                        yhteispaino += int(s.paino)  
                        print(s.nimi, s.paino)
                        kutsuMua(lapsi)
        print("yht.paino", yhteispaino)
            



readfile()
#print(data)
teeDic()
muodostaLuokat()
lapseta()
laskePaino()