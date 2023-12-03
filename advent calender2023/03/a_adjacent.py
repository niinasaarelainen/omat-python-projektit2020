data = []
ei_vieressa = 0
erikoismerkit = []
ymparykset = []


def readfile():
    f = open("data.txt", "r")         
    for rivi in f:
        data.append(rivi.strip())    


def erikoismerkit_muistiin():
    for y in range(len(data)):
        for x in range(len(data[y])):
            if not data[y][x].isdigit() and not data[y][x] == '.':
                erikoismerkit.append([y, x])


def ymparykset_muistiin():
    global ymparykset
    for merkki in erikoismerkit:
        ym, xm = merkki
        for y in range(ym-1, ym+2):
            for x in range(xm-1, xm+2):
                ymparykset.append([y, x])        


def tutki():
    global ei_vieressa, ymparykset
    
    for y in range(len(data)):
        muistiin = False
        luku_meneillaan = ""
        x = 0
        while x < len(data[y]):
            while x < len(data[y]) and data[y][x].isdigit() : 
                #print(x, muistiin)
                luku_meneillaan += data[y][x]
                if [y, x] in ymparykset:
                    muistiin = True  
                x += 1                      

            if muistiin and luku_meneillaan != "":
                print(int(luku_meneillaan))
                ei_vieressa += int(luku_meneillaan)
                luku_meneillaan = ""             
                muistiin = False

            x += 1
            luku_meneillaan = ""   




readfile()
erikoismerkit_muistiin()
ymparykset_muistiin()
tutki()
print(ei_vieressa)    # 509115