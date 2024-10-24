
positions = [4, 8]     # 4-->7 !!!
die_roll_count = 0
scores = [0, 0]
pawn1 = 0
pawn2 = 0
menossa_lukema = 1

def heita():
    global menossa_lukema, score1, score2, die_roll_count, positions
    
    for kumman_vuoro in range(2):
        valitulos = 0
        
        for i in range(3):
            die_roll_count += 1
            if die_roll_count >= 1000:
                print("moi")        # TODO  !?!?!?!!??!?!
                return die_roll_count
            valitulos += menossa_lukema
            menossa_lukema += 1
            if menossa_lukema > 100:
                menossa_lukema = 1
        
        print("valitulos", valitulos)
        positions[kumman_vuoro % 2] += valitulos - 1
        positions[kumman_vuoro % 2] = positions[kumman_vuoro % 2] % 10 + 1
        scores[kumman_vuoro % 2] += positions[kumman_vuoro % 2]
        
    print(scores)
    print("positions", positions)
    return die_roll_count




while max(scores) < 1000:
    count = heita()
print(count)

print(scores)
print(die_roll_count)