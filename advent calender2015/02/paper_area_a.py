
data = []



def readfile():
    f = open("data.txt", "r")   # ULRD
    for rivi in f:
        data.append(rivi.strip())


def x():
    
    total = 0

    for r in data:       
        l, w, h = r.split("x")
        l = int(l)
        w = int(w)
        h = int(h)
        area = (2*l*w) + (2*w*h) + (2*h*l)

        mitat = [l, w, h]
        mitat = sorted(mitat)
        extra = mitat[0] * mitat[1]

        total += area + extra

    return total


readfile()
print(x())


#a = map(str, koodit)    
#print(''.join(a))
 
