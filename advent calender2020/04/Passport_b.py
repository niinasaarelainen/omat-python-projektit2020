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
            if lisatutkimukset(hlo, kentta) == False:
                not_valid += 1   
                break 

    return (len(kaikki_henkilot) - not_valid)        


def lisatutkimukset(hlo, kentta):

    #byr (Birth Year) - four digits; at least 1920 and at most 2002.
    if kentta == "byr":
        if not 1920 <= int(hlo[kentta]) <= 2002:
            print("byr false")
            return False    

    #iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    elif kentta == "iyr":
        if not 2010 <= int(hlo[kentta]) <= 2020:
            print("iyr false")
            return False    

    #eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    elif kentta == "eyr":
        if not 2020 <= int(hlo[kentta]) <= 2030:
            print("eyr false")
            return False   

    #hgt (Height) - a number followed by either cm or in:
    #If cm, the number must be at least 150 and at most 193.
    #If in, the number must be at least 59 and at most 76.
    elif kentta == "hgt":
        pituus_ja_mittayksikko = hlo[kentta]
        if len(pituus_ja_mittayksikko) < 4:
            return False
        print("pituus_ja_mittayksikko", pituus_ja_mittayksikko)
        mittayksikko = pituus_ja_mittayksikko[-2:]
        pituus = int(pituus_ja_mittayksikko[:-2])
        if mittayksikko not in ["cm", "in"]:
            return False
        if mittayksikko == "cm":
            if not 150 <= pituus <= 193:
                print("cm false")
                return False   
        if mittayksikko == "in":
            if not 59 <= pituus <= 76:
                print("in false")
                return False   

    #hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    elif kentta == "hcl":
        color =  hlo[kentta]
        eka = color[0]
        if eka != "#":
            print("# puuttuu at hcl")            
            return False  
        if len(color[1:]) != 6:
            print("liian lyhyt at hcl")            
            return False 
        for kirjain in color[1:]:
            if kirjain not in "0123456789abcdef":
                print("väärä merkki at hcl")            
                return False 

    #ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    elif kentta == "ecl":
        if hlo[kentta] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            print("silmänväri !")            
            return False 

    #pid (Passport ID) - a nine-digit number, including leading zeroes.
    elif kentta == "pid":
        pid = hlo[kentta]
        if len(pid) != 9:
            print("pid väärän pituinen")            
            return False 
        for merkki in pid:
            if merkki not in "0123456789":
                print("pid väärä merkki", merkki)            
                return False 



readfile()
print(kasittele_dict())
