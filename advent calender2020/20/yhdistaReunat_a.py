data_temp = []
data = {}
data_rev = {}    # sama data, key-->value
jarjestys = {}  # 


def readfile():      
    f = open("data_1.txt", "r")         
    for rivi in f:
        if rivi.strip() != '':
            data_temp.append(rivi.strip())
    print(data_temp)


def muodostaData():
    global data
    
    key = 0
    for i in range(len(data_temp)):
        if " " in data_temp[i]:
            if key != 0:
                data[key] = kuvio
                data_rev[kuvio[0]] = key
            kuvio = []
            sp = data_temp[i].split(" ")
            key = sp[1][0:4]            
        else:
            kuvio.append(data_temp[i])
            print(kuvio)
    data[key] = kuvio
    data_rev[kuvio[0]] = key


def etsiKeskimmainen(kuviot):
    for kuvio in kuviot:
        print(kuvio)


readfile()
muodostaData()
for item in data.items():
    print(item)

etsiKeskimmainen(data.values())

