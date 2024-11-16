data = []
oliot = []
ore_summa = 0
symbolit = {}

class Tarvitsen:

    def __init__(self, symboli, maara, tarvitsen= []) -> None:
        self.symboli = symboli
        self.maara = maara
        self.tarvitsen = tarvitsen

    def __repr__(self) -> str:
        return f"{self.symboli}, {self.maara}, {self.tarvitsen}"


def readfile():
    global data
    f = open("data_2.txt", "r") 
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
        if symboli not in symbolit:
            symbolit[symboli] = 0
    

def kay_lapi():
    for olio in oliot:
        value_nyt = olio.tarvitsen
        print(value_nyt)
        for tarvitsen in value_nyt:
            if tarvitsen.symboli != "ORE":
                o2 = [olio for olio in oliot if olio.symboli == tarvitsen.symboli]
                o2[0].maara *= tarvitsen.maara
                print(o2[0].maara, tarvitsen.maara)
                symbolit[tarvitsen.symboli] += tarvitsen.maara * olio.maara
                print("tarvitsen", tarvitsen.symboli, tarvitsen.maara , olio.maara)
            print(oliot)

                
    print(symbolit)

    """
    if "ORE" in value_nyt :
        return
    value_nyt = hash_toisinpain[key_nyt][0]
    
    for item in value_nyt:
        print("item", item)
        kay_lapi(item.split(" ")[1])


    print("ulkona")  """



readfile()
tee_oliot()
print(oliot)
kay_lapi()   # data2: {'FUEL': 1, 'AB': 2, 'BC': 3, 'CA': 4, 'C': 37, 'A': 10, 'B': 23}