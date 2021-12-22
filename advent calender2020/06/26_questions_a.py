
all_answers = []


def readfile():  
    f = open("data.txt", "r")     
    group = []    
    for rivi in f:
        if rivi.strip() == "":
            all_answers.append(group)
            group = []   
        else:
            group.append(rivi.strip())
    all_answers.append(group)    
    

def tutki():
    pituudet = []
    for group in all_answers:
        eri_kirjaimet = []
        for answer in  group:
            for kirjain in answer:
                if kirjain not in eri_kirjaimet:
                    eri_kirjaimet.append(kirjain)
        pituudet.append(len(eri_kirjaimet))
    return pituudet

readfile()
print(all_answers)   
print(sum(tutki()))