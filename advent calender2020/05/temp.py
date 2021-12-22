def ohjeet_oikea_rivi():
    columns_min = 0
    columns_max = columns - 1
    for rivi in data:
        ohje = rivi[7:]
        for kirjain in ohje:
            vali = columns_max - columns_min
            if kirjain == "R":
                columns_min = columns_min + vali  // 2 + 1
            if kirjain == "L":
                columns_max = columns_max - vali  // 2 - 1
            print(kirjain, columns_min, columns_max )

    return columns_max   # min = max, voisi palauttaa kumman vain