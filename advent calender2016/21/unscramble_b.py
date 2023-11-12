#word= "abcdefgh"  #oikea, 8
word = "decab"    #helppo, 5     data_a tämän kanssa
word = "abcde"    #helppo, 5     data_a tämän kanssa
word = "deabc"    #helppo, 5     data_a tämän kanssa
data = []


def readfile(): 
    f = open( "data_test.txt", "r") 
    for rivi in f:
        data.append(rivi.strip())


def swap(sanat): # ei muuteta
    global word
    if ord(sanat[2]) < 97:   # lukuja
        pos1 = min(int(sanat[2]), int(sanat[5]))
        temp1 = word[pos1]
        pos2 = max(int(sanat[2]), int(sanat[5]))
        temp2 = word[pos2]
        word = word[:pos1] + temp2 + word[pos1 + 1:pos2] + temp1 + word[pos2 + 1:]
    else:                   # kirjaimia
        pos1 = min(word.index(sanat[2]), word.index(sanat[5]))
        temp1 = word[pos1]
        pos2 = max(word.index(sanat[2]), word.index(sanat[5]))
        temp2 = word[pos2]
        word = word[:pos1] + temp2 + word[pos1 + 1:pos2] + temp1 + word[pos2 + 1:]

def reverse(sanat): # ei muuteta
    global word
    pos1 = int(sanat[2])
    pos2 = int(sanat[4])
    rev = word[pos1:pos2+1][::-1]
    word = word[:pos1] + rev + word[pos2 + 1:]

def rotatate_based_on_position(kirjain, sana):
    print("sana:", sana)
    ind = sana.index(kirjain)
    maara = 1 + ind 
    if ind >= 4:   
        maara += 1
    for i in range(maara):
        tulos = sana[-1:] + sana[:-1]    # oli -1
    print("tulos", tulos)
    return tulos

def rotate(sanat):
    global word
    if len(sanat) == 4:    # 'rotate', 'left', '1', 'step'
        suunta = sanat[1]
        maara = int(sanat[2])
        if suunta == "right":  # R ja L vaihtoivat paikkaa
            word = word[maara:] + word[:maara]
        if suunta == "left":
            word = word[-maara:] + word[:-maara]

    else :                # 'rotate', 'based', 'on', 'position', 'of', 'letter', 'd'
        #testataan 1-4 vas
        for maara in range(4):
            testword = word[maara:] + word[:maara]
            print(maara, testword, word)
            if word == rotatate_based_on_position(sanat[6], testword):
                print(" !! yeah", maara, sanat[6])
        

def move(sanat):
    global word
    pos1 = int(sanat[2])
    kirjain = word[pos1]
    pos2 = int(sanat[5])
    sana_miinus_kirjain =  word.replace(kirjain, "")
    word = sana_miinus_kirjain[:pos2] + kirjain + sana_miinus_kirjain[pos2:]


def lue():    
    for rivi in reversed(data):
        print(rivi)
        sanat = rivi.split(" ")
        
        if "rotate" in rivi:
            rotate(sanat)

        if "swap" in rivi:   
            swap(sanat)   

        if "reverse" in rivi:
            reverse(sanat)

        if "move" in rivi:
            move(sanat)

        print(word, "\n")


readfile()
lue()     # ei cagbefdh   chaebgfd
