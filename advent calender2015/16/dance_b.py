stringi = "abcdefghijklmnop"
orig = stringi = "abcdefghijklmnop"
stringi = [char for char in stringi]
orig = [char for char in orig]
pit = len(stringi)
data = []  

def readfile():
    f = open( "data.txt", "r") 
    for rivi in f:
        rivi = rivi.strip()
        sp = rivi.split(",")
        for s in sp:
            data.append(s)

def spin(maara):   # s3  abcde --> cdeab
    global stringi 
    alku = stringi[:pit-maara]
    loppu = stringi[pit-maara:]
    stringi = loppu + alku

def exchange(pos1, pos2):  # at positions A and B swap places
    global stringi
    temp = stringi[pos1]
    stringi[pos1] = stringi[pos2]
    stringi[pos2] = temp

def partner(name1, name2):  # programs named A and B swap places
    ind1 = stringi.index(name1)
    ind2 = stringi.index(name2)
    exchange(ind1, ind2)



def find():
    for i in range(40):   
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
                partner (sp[0], sp[1])
        


readfile()
montako = 1000000000 % 60
print(montako)
find() 
s = "".join(str(x) for x in stringi)
print(s)


