
data = []


def readfile():
    f = open("data.txt", "r") 
    for rivi in f:
        data.append(rivi.strip())


def tutki():
   garbagea = False
   g_start = 0
   for rivi in data:
        i = 0
        groups = 0
        score = 0
        print(rivi)
        while i <= len(rivi) -1:
            if rivi[i] == "<":
                garbagea = True
            elif rivi[i] == ">":
                garbagea = False
            elif rivi[i] == "!":
                i += 1
            elif rivi[i] == "{" and not garbagea:
                g_start += 1
            elif rivi[i] == "}" and g_start >0 and not garbagea:
                score += g_start
                g_start -= 1
                groups += 1
            i += 1
        print(groups, score)
    


readfile()
tutki()
