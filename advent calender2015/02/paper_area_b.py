
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
        bow = l * w * h
        print("bow", bow)

        mitat = [l, w, h]
        mitat = sorted(mitat)
        m1 = mitat[0] 
        m2 = mitat[1]
        wrap = m1 + m1 + m2 + m2
        print("wrap", wrap)

        total += bow + wrap

    return total


readfile()
print(x())


#a = map(str, koodit)    
#print(''.join(a))
 
