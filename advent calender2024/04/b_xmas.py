from collections import defaultdict

data = []
montako = 0


def readfile():
    f = open("data_1.txt", "r")   # data_1 = 18
    for rivi in f:
        data.append(rivi.strip())


def diag(matrix):
    global montako
    loytyyko_kaksi = 0

    diagonal1 = defaultdict(list) # For the top right to bottom left
    diagonal2 = defaultdict(list) # For the top left to bottom right
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            diagonal1[i-j].append(matrix[i][j])
            diagonal2[i+j].append(matrix[i][j])

    v1 = ["".join(v) for v in diagonal1.values()]
    v2 = ["".join(v) for v in diagonal2.values()]

    for rivi in v1:
        loytyyko_kaksi += rivi.count("MAS")
        loytyyko_kaksi += rivi.count("SAM")  

    for rivi in v2:
        loytyyko_kaksi += rivi.count("MAS")
        loytyyko_kaksi += rivi.count("SAM")  

    if loytyyko_kaksi == 2:
        montako += 1
    
    
def pilko_3x3():

    for aloitus_y in range(0, len(data) -2):
        for aloitus_x in range(0, len(data) -2):
            kolmexkolme = []
            for y in range(3):
                rivi = ""
                for x in range(3):
                    rivi += data[aloitus_y + y][aloitus_x + x]
                kolmexkolme.append(rivi)
            diag(kolmexkolme)
            print(kolmexkolme)



readfile()
pilko_3x3()

print(montako)