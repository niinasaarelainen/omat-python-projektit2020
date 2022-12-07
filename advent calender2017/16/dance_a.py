str = "abcde"
pit = len(str)
data = []  

def readfile():
    f = open( "data_a.txt", "r") 
    for rivi in f:
        rivi = rivi.strip()
        data.append(rivi)

def spin(maara):   # s3  abcde --> cdeab
    global str
    alku = str[:pit-maara]
    loppu = str[pit-maara:]
    str = loppu + alku
    print(str)

def exchange(pos1, pos2):  # at positions A and B swap places
    print(pos1, pos2)

def partner(name1, name2):  # programs named A and B swap places
    print(name1, name2)


def find():
    for rivi in data:
        if "s" in rivi:
            rivi = rivi[1::]            
            spin(int(rivi))
        if "x" in rivi:
            rivi = rivi[1::]
            sp = rivi.split("/")
            exchange (int(sp[0]), int(sp[1]))
        if "p" in rivi:
            rivi = rivi[1::]
            sp = rivi.split("/")
            exchange (sp[0], sp[1])


readfile()
print(data)
find() 
spin(3)
    


