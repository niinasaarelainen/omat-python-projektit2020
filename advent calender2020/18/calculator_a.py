data = []

"""
1 + 2 * 3 + 4 * 5 + 6
  3   * 3 + 4 * 5 + 6
      9   + 4 * 5 + 6
         13   * 5 + 6
             65   + 6
                 71     """


def readfile():   # a-kohta
    global data
    f = open("data_easy.txt", "r")         
    for rivi in f:
        data.append(rivi.split(" "))
    print(data)


def calculate():
    global data

    edellinen = None
    tulos = 0

    for rivi in data:
        for i in range(len(rivi) - 1):
            if rivi[i] == "+":
                tulos += tulos + int(rivi[i + 1])  
            elif rivi[i] == "*":
                tulos += tulos * int(rivi[i + 1])  
            elif rivi[i] == "(":
                pass
            elif rivi[i] == ")":
                pass
            else:
                pass

            print(tulos)



readfile()
calculate()
print()
