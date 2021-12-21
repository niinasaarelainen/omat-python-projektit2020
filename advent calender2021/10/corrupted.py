import math

lines = []
points_hash = {")": 3, "]": 57, "}": 1197, ">": 25137}

def readfile():   # a-kohta
    f = open("data.txt", "r")         
    for rivi in f:
            lines.append(rivi.strip())

def corrupted():
    aloittavat_merkit = "([{<"
    corrupted_lines = []
    virhemerkit = []
    
    for line in lines:
        muistiin = []
        for merkki in line:
            if merkki in aloittavat_merkit:
                muistiin.append(merkki)
            elif merkki == ")":
                if muistiin[-1] == "(":
                    muistiin.pop(-1)
                else:
                    corrupted_lines.append(line)
                    virhemerkit.append(merkki)
                    break
            elif merkki == "}":
                if muistiin[-1] == "{":
                    muistiin.pop(-1)
                else:
                    corrupted_lines.append(line)
                    virhemerkit.append(merkki)
                    break
            elif merkki == "]":
                if muistiin[-1] == "[":
                    muistiin.pop(-1)
                else:
                    corrupted_lines.append(line)
                    virhemerkit.append(merkki)
                    break
            elif merkki == ">":
                if muistiin[-1] == "<":
                    muistiin.pop(-1)
                else:
                    corrupted_lines.append(line)
                    virhemerkit.append(merkki)
                    break


    return virhemerkit

def count_points(virhemerkit):
    points = 0
    for merkki in virhemerkit:
        points += points_hash[merkki]
    print(points)


readfile()
count_points(corrupted())
