
positions = [4, 8]     # 4-->7 !!!
positions = [7, 8]
die_roll_count = 0
scores = [0, 0]
pawn1 = 0
pawn2 = 0
menossa_lukema = 1
vastaus = 0

def heita(kumman_vuoro):
    global menossa_lukema, die_roll_count, vastaus       
    valitulos = 0        
    for i in range(3):
        die_roll_count += 1
        
        valitulos += menossa_lukema
        menossa_lukema += 1
        if menossa_lukema > 100:
            menossa_lukema = 1
    
    print("valitulos", valitulos)
    positions[kumman_vuoro % 2] += valitulos - 1
    positions[kumman_vuoro % 2] = positions[kumman_vuoro % 2] % 10 + 1
    scores[kumman_vuoro % 2] += positions[kumman_vuoro % 2]
    if max(scores) >= 1000:
        print("    hep")
        vastaus = die_roll_count
        print("vastaus", vastaus)
        
    print("scores", scores)
    print("positions", positions)
    return vastaus



kumman_vuoro = 0
while vastaus == 0 :      # 1000
    print("kumman_vuoro", kumman_vuoro, "vastaus", vastaus)
    vastaus = heita(kumman_vuoro)
    print("vastaus", vastaus)
    kumman_vuoro += 1
print("vastaus", vastaus)

print("scores", scores)
print(die_roll_count)
print(vastaus * min(scores))