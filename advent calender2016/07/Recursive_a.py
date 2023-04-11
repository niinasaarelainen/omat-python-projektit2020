
data = []
dic = {}



def readfile():
    f = open("data.txt", "r") 
    for rivi in f:
        rivi = rivi.strip()
        if "->" in rivi:
            data.append(rivi.split("->"))

def teeDic():
    for rivi in data:
        dic[rivi[0].split(" ")[0]] = rivi[1].replace(",", "").split(" ")

    #print(dic)


def tutkiDic():
    for item in dic:
        ei_loytynyt = True
        for array in dic.values():
            for v in array:
                if item == v:
                    ei_loytynyt = False
        if ei_loytynyt:
            print(item)


readfile()
#print(data)
teeDic()
tutkiDic()