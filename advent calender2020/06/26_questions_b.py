
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
    yes = 0
    for group in all_answers:
        eka_vastaus = group[0]
        print("eka_vastaus", eka_vastaus)
        for letter in eka_vastaus:
            kirjain_kaikilla = True
            for answer in group:  
                if letter not in  answer:                   
                    print("Fail  !!  ")
                    kirjain_kaikilla = False
            if kirjain_kaikilla:
                yes += 1    
            
    return yes

readfile()
print(all_answers)   
print(tutki())