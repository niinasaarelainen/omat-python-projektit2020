import hashlib

data = "pgflpeqp"  # puzzle input
data = "hijkl"
kuva = []
mina_y = 1
mina_x = 1
kohde_y = 4
kohde_x = 4
pakita = {"R": "L", "L": "R", "U":"D", "D":"U"}


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

def circulate():
    global data
    result = hashlib.md5(data.encode())
    res = result.hexdigest()[:4]
    print(res)
    if ord(res[1]) >= 98 and ord(res[1]) <= 102:  # up, down, left, and right
        if kuva[mina_y + 1][mina_x] == 0:
            mina_y + 1
            data += "D"
    elif ord(res[3]) >= 98 and ord(res[3]) <= 102:  # up, down, left, and right
        if kuva[mina_y][mina_x + 1] == 0:
            mina_x + 1
            data += "R"
    elif ord(res[0]) >= 98 and ord(res[0]) <= 102:  # up, down, left, and right
        if kuva[mina_y - 1][mina_x] == 0:
            mina_y - 1
            data += "U"
    elif ord(res[3]) >= 98 and ord(res[3]) <= 102:  # up, down, left, and right
        if kuva[mina_y][mina_x - 1] == 0:
            mina_x - 1
            data += "L"

        


alusta_kuva()
print_kuva()
#while (mina_y != kohde_y and mina_x != kohde_x):
for i in range(5):
    circulate() 
print(data)


