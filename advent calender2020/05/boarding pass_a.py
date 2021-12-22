data = []
rows = 128 
columns = 8
"""
BFFFBBFRRR: row 70, column 7, seat ID 567.
FFFBBBFRRR: row 14, column 7, seat ID 119.
BBFFBBFRLL: row 102, column 4, seat ID 820. """

def readfile():
    f = open("data.txt", "r") 
    for rivi in f:
        data.append(rivi.strip())

"""Start by considering the whole range, rows 0 through 127.
F means to take the lower half, keeping rows 0 through 63.
B means to take the upper half, keeping rows 32 through 63.
F means to take the lower half, keeping rows 32 through 47.
B means to take the upper half, keeping rows 40 through 47.
B keeps rows 44 through 47.
F keeps rows 44 through 45.
The final F keeps the lower of the two, row 44."""

def ohjeet_oikea_rivi(rivi):
    rows_min = 0
    rows_max = rows - 1
    ohje = rivi[:7]
    for kirjain in ohje:
        vali = rows_max - rows_min
        if kirjain == "B":
            rows_min = rows_min + vali  // 2 + 1
        if kirjain == "F":
            rows_max = rows_max - vali  // 2 - 1

    return rows_max   # min = max, voisi palauttaa kumman vain



def ohjeet_oikea_tuoli(rivi):
    columns_min = 0
    columns_max = columns - 1
    ohje = rivi[7:]
    for kirjain in ohje:
        vali = columns_max - columns_min
        if kirjain == "R":
            columns_min = columns_min + vali  // 2 + 1
        if kirjain == "L":
            columns_max = columns_max - vali  // 2 - 1

    return columns_max   # min = max, voisi palauttaa kumman vain



readfile()
highest = 0
for rivi in data:
    r = ohjeet_oikea_rivi(rivi)
    t = ohjeet_oikea_tuoli(rivi)
    if r * 8 + t > highest:
        highest =  r * 8 + t

print(highest)  