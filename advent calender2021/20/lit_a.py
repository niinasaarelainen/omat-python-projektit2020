import copy

data = []  
algo = ""
uusiKuva = []


def readfile():   # a-kohta
    global algo, uusiKuva
    data_temp = []
    f = open("data.txt", "r")         
    for rivi in f:
        rivi = "..." + rivi.strip() + "..."
        data_temp.append(rivi)

    rivinPituus = len(data_temp[0])
    rivi = ['.' for tyhja in range(rivinPituus)]
    data_temp.insert(0, rivi)
    data_temp.insert(0, rivi)
    data_temp.insert(0, rivi)
    data_temp.append(rivi)
    data_temp.append(rivi)
    data_temp.append(rivi)

    for rivi in data_temp:
        uusirivi = []
        for merkki in rivi:
            uusirivi.append(merkki)
        data.append(uusirivi)

    uusiKuva = copy.deepcopy(data)
    
    f = open("algo.txt", "r")         
    for rivi in f:
        algo += rivi.strip()


def laskeYsiköt():
    for y in range(len(data)):    
        for x in range(len(data[0])):
            tutkittava = [y, x]
            nine = ""
            for y3 in range(-1, 2):   # -1,0,1
                for x3 in range(-1, 2):
                    if y3 + y < 0 or x3 + x < 0 or y3 + y >= len(data) or x3 + x >= len(data[0]):
                        nine += "."
                    else:
                        nine += data[y+y3][x+x3]
            binary(nine, tutkittava)


def binary(stringi, tutkittava):
    binary = ""
    y, x = tutkittava
    for merkki in stringi:
        if merkki == ".":
            binary += "0"
        else:
            binary += "1"
    monesko = int(binary, 2)
    uusiKuva[y][x] = algo[monesko]    



readfile()

hashtageja = 0
for rivi in data:
    #print(rivi)
    hashtageja += rivi.count('#')

print(hashtageja)   
laskeYsiköt()

data = copy.deepcopy(uusiKuva)
laskeYsiköt()
print()

hashtageja = 0
for rivi in uusiKuva:
    hashtageja += rivi.count('#')



print(hashtageja)     # 5169 too low,   5232 too high


