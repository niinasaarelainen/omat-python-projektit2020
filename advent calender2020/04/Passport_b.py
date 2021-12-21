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
                elif lisatutkimukset():
                    not_valid += 1
                else:    
                    not_valid += 1
                break

    return (len(kaikki_henkilot) - not_valid)        


def lisatutkimukset():
    #byr (Birth Year) - four digits; at least 1920 and at most 2002.

    #iyr (Issue Year) - four digits; at least 2010 and at most 2020.

    #eyr (Expiration Year) - four digits; at least 2020 and at most 2030.

    #hgt (Height) - a number followed by either cm or in:
    #If cm, the number must be at least 150 and at most 193.
    #If in, the number must be at least 59 and at most 76.

    #hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.

    #ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.

    #pid (Passport ID) - a nine-digit number, including leading zeroes.


readfile()
print(kasittele_dict())
