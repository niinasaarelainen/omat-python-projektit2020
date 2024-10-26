
data = []  
algo = ""


def readfile():   # a-kohta
    global algo
    f = open("data_easy.txt", "r")         
    for rivi in f:
        data.append(rivi.strip())
    
    f = open("algo_easy.txt", "r")         
    for rivi in f:
        algo += rivi
    print(algo)


def laskeYsiköt():
    for y in range(len(data)):
        for x in range(len(data[0])):
            tutkittava = [y, x]
            for y3 in range(-1, 2):   # -1,0,1
                for x3 in range(-1, 2):
                    if y3 + y < 0 or x3 + x < 0:
                        print("negaa")

        


readfile()
for rivi in data:
    print(rivi)
laskeYsiköt()

binary = ""
for merkki in "...#...#.":
    if merkki == ".":
        binary += "0"
    else:
        binary += "1"

monesko = int(binary, 2)
#print(algo[monesko])

