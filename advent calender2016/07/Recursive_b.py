
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
suvunpaino = 0
suvunpainot = []
root = None
root_nimi = "tknk"

#TODO toimii data_a:lla mutta ei data:lla,
# huom vaihda root_nimi = uownj

def readfile():
    f = open("data_a.txt", "r") 
    for rivi in f:
        rivi = rivi.strip()
        if "->" in rivi:
            data_lapset.append(rivi.split("->"))
        data_all.append(rivi.replace(" ", ""))




def teeDic():
    for rivi in data_lapset:
        dic[rivi[0].split(" ")[0]] = rivi[1].replace(",", "").strip().split(" ")

    #print(dic)


def muodostaLuokat():
    global root
    for rivi in data_all:
        nimi, paino = rivi.split("(")
        paino, loput = paino.split(")")
        solut.append(Solu(nimi.replace(" ", ""), paino.replace(")", "")))

    nimet = [s.nimi for s in solut]
    print(nimet)
    painot = [s.paino for s in solut]
    print(painot)
    root = [s for s in solut if s.nimi == root_nimi][0]
    print("root", root)

def lapseta():
    for item in dic:
        [s.lapseta(dic[item]) for s in solut if s.nimi == item]
        
    lapset = [s.lapset for s in solut]    
    print(lapset)

def laskePaino():
    """
    ugml + (gyxo + ebii + jptl) = 68 + (61 + 61 + 61) = 251
    padx + (pbga + havc + qoyq) = 45 + (66 + 66 + 66) = 243
    fwft + (ktlj + cntj + xhth) = 72 + (57 + 57 + 57) = 243   """

    def kutsuMua(nimi):
        global  suvunpainot
        for s in solut:
            if  nimi in s.nimi:
                lapset = s.lapset 
        print(lapset)
        for lapsi in lapset:        
            if lapsi != "":
                for s in solut:
                    if  lapsi in s.nimi:
                        suvunpainot.append(int(s.paino))
                        print(s.nimi, s.paino)
                        kutsuMua(lapsi) 
            
    kutsuMua(root_nimi)
    print("suvunpainot", suvunpainot)
    print(len(root.lapset))
    

def suvunPainot():
    i = 0
    yht = 0
    painot = []
    jakaja = int(len(suvunpainot)/len(root.lapset))
    for p in suvunpainot:
        yht += p
        if i % jakaja == jakaja - 1:
            i = 0
            painot.append(yht)
            yht = 0
        else:
            i += 1            
    ind = painot.index((max(painot)))
    erotus = max(painot) - min(painot)
    vaara_luku = suvunpainot[(ind * jakaja)]
    print(vaara_luku - erotus)

            



readfile()    # uownj
#print(data)
teeDic()
muodostaLuokat()
lapseta()
laskePaino()
suvunPainot()