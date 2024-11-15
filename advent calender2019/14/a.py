data = []
oliot = []
ore_summa = 0

class Tarvitsen:

    def __init__(self, symboli, maara, tarvitsen= []) -> None:
        self.symboli = symboli
        self.maara = maara
        self.tarvitsen = tarvitsen

    def __repr__(self) -> str:
        return f"{self.symboli}, {self.maara}, {self.tarvitsen}"


def readfile():
    global data
    f = open("data_1.txt", "r") 
    for rivi in f:
        data.append(rivi.strip())


def tee_oliot():
    for rivi in data:
        a, b = rivi.split(" => ")  # 7 A, 1 B => 1 C
        print(a, b)
        maara, symboli = b.split(" ")
        mita_tarvitsen = []
        if "," in a:           
            for item in a.split(", "):
                m, s = item.split(" ")
                mita_tarvitsen.append(Tarvitsen(s, int(m)))            
        else:
            m, s = a.split(" ")
            mita_tarvitsen.append(Tarvitsen(s, int(m)))
        oliot.append(Tarvitsen(symboli, int(maara), mita_tarvitsen))
    

def kay_lapi(k):
    key_nyt = k
    value_nyt = hash_toisinpain[key_nyt]

    if "ORE" in value_nyt :
        return
    value_nyt = hash_toisinpain[key_nyt][0]
    
    for item in value_nyt:
        print("item", item)
        kay_lapi(item.split(" ")[1])


    print("ulkona")



readfile()
tee_oliot()
print(oliot)
#kay_lapi("FUEL")