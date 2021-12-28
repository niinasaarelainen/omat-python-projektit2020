data = []

"""
1 + (2 * 3) + (4 * (5 + 6))
1 +    6    + (4 * (5 + 6))
     7      + (4 * (5 + 6))
     7      + (4 *   11   )
     7      +     44
            51    """


def readfile():   # a-kohta
    global data
    f = open("data_sulut.txt", "r")         
    for rivi in f:
        rivi = rivi.replace("(", " ( ")
        rivi = rivi.replace(")", " ) ")
        rivi = rivi.replace("  ", " ")    # 2 tyhjää pois
        data.append(rivi.strip().split(" "))
    print(data)


def calculate(tulos):
    global data
    eka_nro = data[0][0]
    
    # sulkujen läpikäynti
    alkusulut = []
    loppusulut = []
    suluton_data = []
    for rivi in range(len(data)):
        for i in range(len(data[rivi]) ):
            if "(" in data[rivi][i]:     
                alkusulut.append(i)
            elif ")" in  data[rivi][i]:
                loppusulut.append(i)
            else: 
                suluton_data.append(data[rivi][i])

    print(alkusulut, loppusulut, suluton_data)   # sulkujen indeksit eivät päde tänne

    for rivi in data:
        for i in range(len(rivi) - 1):
            if rivi[i] == "+":
                if tulos == 0:
                    tulos = eka_nro + int(rivi[i + 1])  
                else:
                    tulos += int(rivi[i + 1])  
            elif rivi[i] == "*":
                if tulos == 0:
                    tulos = eka_nro * int(rivi[i + 1])  
                else:
                    tulos *=  int(rivi[i + 1])  
            elif rivi[i] == "(":     # TODO huom voi olla ((  ennen )
                pass
            elif rivi[i] == ")":
                pass
            """
            elif tulos == 0:
                tulos = int(rivi[i])   """

            print(tulos)



readfile()
calculate(0)  # tulos aluksi 0
print()
