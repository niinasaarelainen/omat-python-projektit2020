import math

lines = []
points_hash = {")": 1, "]": 2, "}": 3, ">": 4}



def readfile():   # a-kohta
    #f = open("incomplete_lines.txt", "r")    
    f = open("data.txt", "r")                  # 15349342966   too high
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

    return corrupted_lines


def incomplete(corrupted_lines):
    aloittavat_merkit = "([{<"
    puuttuvat_merkit = []
    
    for line in lines:
        if line not in corrupted_lines:
            muistiin = []
            for merkki in line:
                if merkki in aloittavat_merkit:
                    muistiin.append(merkki)
                elif merkki == ")":
                    if muistiin[-1] == "(":
                        muistiin.pop(-1)
                elif merkki == "}":
                    if muistiin[-1] == "{":
                        muistiin.pop(-1)
                elif merkki == "]":
                    if muistiin[-1] == "[":
                        muistiin.pop(-1)
                elif merkki == ">":
                    if muistiin[-1] == "<":
                        muistiin.pop(-1)

            puuttuvat_merkit.append([])
            for merkki in muistiin:            
                if merkki == "(":
                    puuttuvat_merkit[-1].append(")")
                elif merkki == "[":
                    puuttuvat_merkit[-1].append("]")
                elif merkki == "{":
                    puuttuvat_merkit[-1].append("}")
                elif merkki == "<":
                    puuttuvat_merkit[-1].append(">")
            puuttuvat_merkit[-1].reverse()
    
    for rivi in puuttuvat_merkit:
        print(rivi)
    return puuttuvat_merkit


def count_points(puuttuvat_merkit):
    scores = []
    
    for rivi in puuttuvat_merkit:
        points = 0
        for merkki in rivi:
            points *= 5
            points += points_hash[merkki]
        scores.append(points)
    return scores


readfile()
c_lines = corrupted()
scores = count_points(incomplete(c_lines))
scores.sort()
print(scores[len(scores)//2])
