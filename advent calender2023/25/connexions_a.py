data = [] 
connexions = {}


def readfile():   
    f = open("data_1.txt", "r")         
    for rivi in f:
        data.append(rivi.strip().split(": "))


def muodosta_hash():
    for rivi in data:
        key, value = rivi
        sp = value.split(" ")
        connexions[key] = sp

        for s in sp:
            if s not in connexions:
                connexions[s] = [key]
            else:
                connexions[s].append(key)
    

def rerun_hash():
    for key, values in connexions.items():
        for v in values:
            if v not in connexions:
                connexions[v] = [key]
            elif key not in connexions[v]:
                connexions[v].append(key)


def disconnect(eka, toka):
    connexions[eka].remove(toka)
    connexions[toka].remove(eka)
    print(connexions)


def groups(montako):
    oli_jo = []
    for key, values in connexions.items():
        #oli_jo.append(key)
        for monesko in range(montako):    
            #print(monesko)   
            #print(oli_jo)   
            while key not in oli_jo:
                print(connexions[key][monesko])      
                key = connexions[key][monesko] 
                oli_jo.append(key)

    print(orig_len, len(oli_jo))
    if orig_len == len(oli_jo):
        print("kaikki")       


def groups2(montako, key):
    oli_jo = []    
    
    
    for monesko in range(montako):  
        oli_jo.append(key)
        key = connexions[key][monesko]  
        #print(monesko)   
        #print(oli_jo)   
        while key not in oli_jo:
            print(connexions[key][monesko])      
            key = connexions[key][monesko] 
            oli_jo.append(key)

    print(orig_len, len(oli_jo))
    if orig_len == len(oli_jo):
        print("kaikki")             


    

readfile()
muodosta_hash()
print(connexions)
print()
rerun_hash()
orig_len = len(connexions)
#print(connexions)

groups2(4, "jqt")
print() 
groups(4)
print() 
groups2(4, "hfx") 
disconnect("hfx", "pzl")
groups2(3, "hfx") 
disconnect("bvb", "cmg")
groups2(3, "hfx") 
disconnect("nvd", "jqt")
groups2(3, "hfx") 
