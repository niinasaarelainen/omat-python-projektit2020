
data = [".^^.^.^^^^"]
data = ["^..^^.^^^..^^.^...^^^^^....^.^..^^^.^.^.^^...^.^.^.^.^^.....^.^^.^.^.^.^.^.^^..^^^^^...^.....^....^."]


def tutki(rivi):  
    uusi_rivi = ""
   
    for i in range(len(rivi)):
        center = rivi[i]
        if i == 0:
            left = "."
            right = rivi[i+1]
        elif i == len(rivi) - 1:
            left = rivi[i-1]
            right = "."
        else:
            left = rivi[i-1]
            right = rivi[i+1]

        #Its left and center tiles are traps, but its right tile is not
        trap1 = (left == "^" and center == "^" and right == ".")
        #Its center and right tiles are traps, but its left tile is not
        trap2 = (left == "." and center == "^" and right == "^")
        #Only its left tile is a trap
        trap3 = (left == "^" and center == "." and right == ".")
        #Only its right tile is a trap
        trap4 = (left == "." and center == "." and right == "^")

        if (trap1 or trap2 or trap3 or trap4):
            uusi_rivi += "^"
        else:
            uusi_rivi += "."
        i += 1     # ..^^.
    data.append(uusi_rivi)


for i in range(399999):
    tutki(data[-1])

safes = 0
for rivi in data:
    safes += rivi.count(".")
print(safes)


