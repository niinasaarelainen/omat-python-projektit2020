
str = "HOH"
muunnokset = [["H", "HO"], ["H", "OH"], ["O", "HH"]]
uudet_sanat = []

def tutki():  
    uusi_str = ""
   
    for ind in range(len(str)):
        uusi_str += str[:ind]
        for muunnos in muunnokset:
            if str[ind] == muunnos[0]:
                uusi_str += muunnos[1]
                uusi_str += str[ind + 1:]
                uudet_sanat.append(uusi_str)
                uusi_str = ""
            else:
                uusi_str += str[ind]
        

tutki()
print(uudet_sanat)

