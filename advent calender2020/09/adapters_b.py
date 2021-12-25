import copy

data = [0]
data_copy = []
highest = 0
one_jolt_differences = 0
three_jolt_differences = 0

def readfile():   # a-kohta
    f = open("data_easy2.txt", "r")         
    for rivi in f:
        data.append(int(rivi.strip()))
    highest = max(data) + 3
    data.append(highest)
    data.sort()
    
    
   

""" 13 lukua
(0), 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, (22)   kaikki
(0), 1, 4, 5, 6, 7, 10, 12, 15, 16, 19, (22)      - 11
(0), 1, 4, 5, 7, 10, 11, 12, 15, 16, 19, (22)     - 6
(0), 1, 4, 5, 7, 10, 12, 15, 16, 19, (22)        - 11 ja 6
(0), 1, 4, 6, 7, 10, 11, 12, 15, 16, 19, (22)    - 5
(0), 1, 4, 6, 7, 10, 12, 15, 16, 19, (22)       - 5 ja 11     tämä puuttuu !!!!!!!!!
(0), 1, 4, 7, 10, 11, 12, 15, 16, 19, (22)      - 5 ja 6
(0), 1, 4, 7, 10, 12, 15, 16, 19, (22)         -5, 6, 11     """ 


# data1_  (0)  1, 4, 5, 6, 7  (9)
def laske_kombot():
    global data, data_copy
    kombot = [data]
    kombo = []
    removed_lkm = 0
    data_copy = copy.deepcopy(data)
    mista_aloitetaan = 1
    # kuinka monta numeroa teoreettisesti voi poistaa
    for montako_poistetaan in range(1, len(data) // 2):   
        print("montako_poistetaan", montako_poistetaan)
        mista_aloitetaan = 1
        removed_lkm = 0
        data_copy = copy.deepcopy(data)
        for mista_aloitetaan in range(1, len(data)- 2):
            removed_lkm = 0
            data_copy = copy.deepcopy(data)
            for ind in range(mista_aloitetaan, len(data)- 1):
                #print("ind", ind)
                if data[ind + 1] - data[ind - 1] <= 3:
                    poistettava = data[ind]
                    print("poistettava", poistettava) 
                    data_copy.remove(poistettava)
                    removed_lkm += 1
                    if removed_lkm == montako_poistetaan or ind == len(data)- 2:
                        #mista_aloitetaan = ind + 1
                        if data_copy not in kombot:
                            kombot.append(data_copy)
                            data_copy = copy.deepcopy(data)
                        else:
                            data_copy.append(poistettava)
                            data_copy.sort()
                            removed_lkm -= 1
                
                
                    

    print(kombot)
    lens = [len(k)  for k in kombot ]
    print(lens)
    print(len(kombot))



readfile()
laske_kombot()   