data = []


def readfile():   
    f = open("data_1.txt", "r")         
    for rivi in f:           
        rivi = rivi.strip()
        data.append(rivi)   

  

readfile()   
print(data)