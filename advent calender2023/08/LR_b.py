data = []
ohje = ""
puu = {}


class StartingNode:

    def __init__(self, node) -> None:
        self.nyky = node


def readfile():  
    f = open("data.txt", "r")  
    for rivi in f:
        data.append(rivi.strip()) 
    
def kasittele_data():
    global ohje
    ohje = data[0]
    for rivi in data[2:]:
        node, lr = rivi.split(" = ")
        l, r = lr.split(", ")
        puu[node] = [l[1:], r[:-1]]
            

def lue_ohjeet():
    nodes = [StartingNode(node) for node in puu if node[-1] == "A"]
    montako_aata = len(nodes)
    print(montako_aata)   # 6
    sijainnit = 0
    osumia = 0
    
    while osumia != montako_aata:
        for kirjain in ohje:
            if osumia == montako_aata:
                return sijainnit

            osumia = 0
            for node in nodes:
                
                if kirjain == "L":
                    node.nyky = puu[node.nyky][0]
                else:
                    node.nyky = puu[node.nyky][1]
                if node.nyky[-1] == "Z":
                    osumia += 1

            if osumia > 3:
                print(node.nyky, osumia)
            sijainnit += 1

    return sijainnit


readfile()
kasittele_data() 
print(puu)
print(lue_ohjeet())