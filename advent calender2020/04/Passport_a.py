import sys

data = []
kaikki_henkilot = []

def readfile():
    henkilon_data = {}
    f = open("data.txt", "r") 
    for rivi in f:
        if rivi.strip() == "":
            kaikki_henkilot.append(henkilon_data)
            henkilon_data = {}
        else:
            rivi = rivi.strip()
            rivi_splitted = rivi.split(" ")   # x määrä  tällaisia  ecl:gry
        
            for item in rivi_splitted:
                key, value = item.split(":")
                henkilon_data[key] =  value
    kaikki_henkilot.append(henkilon_data)


def kasittele_dict():
    vaadittavat_kentat= ["ecl", "pid", "eyr", "hcl", "byr", "iyr", "cid", "hgt"]
    not_valid = 0
    for hlo in kaikki_henkilot:
        print("hlo.keys()", hlo.keys())
        for kentta in vaadittavat_kentat:
            if kentta not in hlo.keys():
                if kentta == "cid":
                    continue
                else:    
                    not_valid += 1
                break

    return (len(kaikki_henkilot) - not_valid)        


readfile()
print(kasittele_dict())
