data = []
erikoismerkit = {}    # ymparykset on value
erikoismerkit_rev = {}  # erikoismerkki on value
tulos = 0


def readfile():
    f = open("data_1.txt", "r")         
    for rivi in f:
        data.append(rivi.strip())    


def erikoismerkit_muistiin():
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == '*':
                erikoismerkit[y, x] = [] # tänne myöhemmin 9 ympäröijää


def ymparykset_muistiin():
    global erikoismerkit
    for merkki in erikoismerkit:
        ym, xm = merkki
        for y in range(ym-1, ym+2):
            for x in range(xm-1, xm+2):
                erikoismerkit_rev[y, x] = merkki   # ympäröijän avulle löytää keskuksen


def tutki():
    
    for y in range(len(data)):
        muistiin = False
        luku_meneillaan = ""
        x = 0
        while x < len(data[y]):
            while x < len(data[y]) and data[y][x].isdigit() : 
                luku_meneillaan += data[y][x]                
                if (y, x) in erikoismerkit_rev:
                    print(erikoismerkit_rev[(y, x)])
                    muistiin = True 
                    tama_muistiin = erikoismerkit_rev[(y, x)]
                x += 1                      

            if muistiin and luku_meneillaan != "":
                print(int(luku_meneillaan))
                erikoismerkit[tama_muistiin].append(int(luku_meneillaan))
                luku_meneillaan = ""             
                muistiin = False

            x += 1
            luku_meneillaan = ""   



readfile()
erikoismerkit_muistiin()
ymparykset_muistiin()

print("erikoismerkit_rev", erikoismerkit_rev)
tutki()
print("erikoismerkit", erikoismerkit)

tasan_kaksi = [v for v in erikoismerkit.values() if len(v) == 2]
for x1, x2 in tasan_kaksi:
    tulos += x1 * x2

print(tulos)  #   467835  75220503