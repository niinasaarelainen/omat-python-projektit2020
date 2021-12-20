
data = []
luvut = []


def readfile():
    f = open("data.txt", "r") 
    for rivi in f:
        data.append(int(rivi.strip()))


def sum_2020():
    loytyi = False
    for i in range(len(data)):
        for j in range(len(data)):
            for k in range(len(data)):
                if data[i] + data[j] + data[k] == 2020 and loytyi == False:
                    luvut.append(data[i])
                    luvut.append(data[j])
                    luvut.append(data[k])
                    loytyi = True

   
    return luvut



readfile()
print(luvut)
print(sum_2020()[0]* sum_2020()[1] * sum_2020()[2])