
data = []


def readfile():   # a-kohta
    f = open("data.txt", "r")         
    for rivi in f:
        data.append(rivi)

def tutki():
    for rivi in data:
        print(rivi)        
        start = 0
        vali = 4
        while start+vali <= len(rivi):
            ok = True
            x =rivi[start : start+vali]
            for char in x :
                counts=x.count(char)
                while counts > 1:
                    ok = False
                    break
            if ok :
                print(start+vali)
                return
            start += 1

# four characters that are all different
readfile()
tutki()

