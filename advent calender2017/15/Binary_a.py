
data = []  
startA = 65
startB =  8921
factorA = 16807
factorB = 48271
div = 2147483647

def readfile():
    f = open( "data_a.txt", "r") 
    for rivi in f:
        rivi = rivi.strip()
        data.append(int(rivi))


def find():
    global data


readfile()
find() 
print(f'{430625591:32b}')   # loppurivi sama, alku ei !!!
print(f'{1092455:32b}')
    


