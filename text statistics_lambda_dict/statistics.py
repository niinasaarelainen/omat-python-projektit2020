

def read_file():
    with open("text_piano") as t:
        for rivi in t:
            if rivi != "\n":
                teksti.append(rivi.strip())


def make_dict(teksti):
    sanat_dict = {}
    for rivi in teksti:
        sanat = rivi.split(" ")
        for sana in sanat:
            if sana.isnumeric():
                continue
            sana = sana.lower()
            for kirjain in sana:
                if kirjain in "()/´'\"\\.,:!?-;":
                    sana = sana.replace(kirjain, "")               
            if sana in sanat_dict:
                sanat_dict[sana] += 1
            else:
                sanat_dict[sana] = 1  
    return sanat_dict            

def top_10(sorted):
    for item in sorted[:10]:
        print(item[0])


def find_partial(sanat_dict, hakusana):
    for sana in sanat_dict:
        if hakusana in sana:
            print(sana, "("+ str(sanat_dict[sana]) +"kpl)")

teksti = []
read_file()

sanat_dict = make_dict(teksti)
sorted_d = sorted(sanat_dict.items(), key=lambda x: x[1])
sorted_d.reverse()
top_10(sorted_d)
find_partial(sanat_dict, "pian")