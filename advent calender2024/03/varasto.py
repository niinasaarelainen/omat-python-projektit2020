def tutki():
    global ei_vieressa, ymparykset
    
    for y in range(len(data)):
        muistiin = False
        luku_meneillaan = ""
        while 
        for x in range(len(data)):
            #print(x, muistiin)
            if [y, x] in ymparykset:
                muistiin = True
            if data[y][x].isdigit():
                luku_meneillaan += data[y][x]
            if data[y][x] == ".":
                if muistiin and luku_meneillaan != "":
                    print(int(luku_meneillaan))
                    ei_vieressa += int(luku_meneillaan)
                    luku_meneillaan = ""
                    muistiin = False

