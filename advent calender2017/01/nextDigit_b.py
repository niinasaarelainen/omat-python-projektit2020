
data = []


def readfile():
    f = open("data.txt", "r") 
    for rivi in f:
        data.append(rivi.strip())


def laske():
    
    

    for rivi in data:
        sum = 0
        valimatka = int(len(rivi)/2)
        for i in range(len(rivi)):
            i2 = (i + valimatka) % len(rivi)
            print(rivi[i] , rivi[i2])            
            if rivi[i] == rivi[i2]:
                sum += int(rivi[i])
        print("summa", sum)

    return sum



readfile()
print(laske())
