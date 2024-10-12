
data = []
luvut = 0


def readfile():
    f = open("data.txt", "r") 
    for rivi in f:
        data.append(rivi)

def summat():
    global luvut
    for rivi in data:
        digits = []
        #luku = 0
        for merkki in rivi:
            if merkki.isdigit():
                digits.append(merkki)
        
        luku = int(digits[0] + digits[-1])
        print(luku)
        luvut += luku



readfile()
summat()
print(luvut)