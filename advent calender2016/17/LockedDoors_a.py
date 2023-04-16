import hashlib

data = "pgflpeqp"  # puzzle input
data = "ihgpwlah"   # DDRRRD
kuva = []
mina_y = 1
mina_x = 1
kohde_y = 4
kohde_x = 4
pakita = {"R": "L", "L": "R", "U":"D", "D":"U"}
kiel_suun = ""


def alusta_kuva():
    kuva.append("######")
    for y in range(4):    # mallissa 7 riviä, oikeasti ???
        rivi = []
        rivi.append("#")
        for x in range(4):
            rivi.append(0)
        rivi.append("#")
        kuva.append(rivi)
    kuva.append("######")

def print_kuva():
    for rivi in kuva:
        for x in rivi:
            print(x, end="")
        print()

def circulate_D_eka():
    global data, mina_x, mina_y, kiel_suun
    print("kiel_suun", kiel_suun)
    result = hashlib.md5(data.encode())
    res = result.hexdigest()[:4]
    print(res)
    if ord(res[1]) >= 98 and ord(res[1]) <= 102 and kiel_suun != "D" and kuva[mina_y + 1][mina_x] == 0:  # up, down, left, and right
            mina_y += 1
            data += "D"
            kiel_suun = ""
    elif ord(res[3]) >= 98 and ord(res[3]) <= 102 and kiel_suun != "R" and kuva[mina_y][mina_x + 1] == 0:  # up, down, left, and right
            mina_x += 1
            data += "R"
            kiel_suun = ""
    elif ord(res[0]) >= 98 and ord(res[0]) <= 102 and kiel_suun != "U" and kuva[mina_y - 1][mina_x] == 0:  # up, down, left, and right
            mina_y -= 1
            data += "U"
            kiel_suun = ""
    elif ord(res[2]) >= 98 and ord(res[3]) <= 102 and kiel_suun != "L" and kuva[mina_y][mina_x - 1] == 0:  # up, down, left, and right
            mina_x -= 1
            data += "L"
            kiel_suun = ""
    else:
        if pakita[data[-1]] == "L":
            mina_x -= 1
        if pakita[data[-1]] == "R":
            mina_x += 1
        if pakita[data[-1]] == "U":
            mina_y -= 1
        if pakita[data[-1]] == "D":
            mina_y += 1
        kiel_suun = data[-1]
        data = data[:-1]
       
def circulate_R_eka():
    global data, mina_x, mina_y, kiel_suun
    print("kiel_suun", kiel_suun)
    result = hashlib.md5(data.encode())
    res = result.hexdigest()[:4]
    print(res)
    if ord(res[3]) >= 98 and ord(res[3]) <= 102 and kiel_suun != "R" and kuva[mina_y][mina_x + 1] == 0:  # up, down, left, and right
            mina_x += 1
            data += "R"
            kiel_suun = ""
    elif ord(res[1]) >= 98 and ord(res[1]) <= 102 and kiel_suun != "D" and kuva[mina_y + 1][mina_x] == 0:  # up, down, left, and right
            mina_y += 1
            data += "D"
            kiel_suun = ""
    elif ord(res[0]) >= 98 and ord(res[0]) <= 102 and kiel_suun != "U" and kuva[mina_y - 1][mina_x] == 0:  # up, down, left, and right
            mina_y -= 1
            data += "U"
            kiel_suun = ""
    elif ord(res[2]) >= 98 and ord(res[3]) <= 102 and kiel_suun != "L" and kuva[mina_y][mina_x - 1] == 0:  # up, down, left, and right
            mina_x -= 1
            data += "L"
            kiel_suun = ""
    else:
        if pakita[data[-1]] == "L":
            mina_x -= 1
        if pakita[data[-1]] == "R":
            mina_x += 1
        if pakita[data[-1]] == "U":
            mina_y -= 1
        if pakita[data[-1]] == "D":
            mina_y += 1
        kiel_suun = data[-1]
        data = data[:-1]
        


alusta_kuva()
print_kuva()
#while (mina_y != kohde_y and mina_x != kohde_x):
for i in range(15):
    circulate_D_eka() 
    print(data)
    print(mina_y, mina_x)
print(data)

data = "ihgpwlah"   # DDRRRD
mina_y = 1
mina_x = 1
kiel_suun = ""
for i in range(15):
    circulate_R_eka() 
    print(data)
    print(mina_y, mina_x)
print(data)


