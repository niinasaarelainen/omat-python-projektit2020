rivi = "3113322113"
data = []

def readfile():
    global data
    f = open("data_1.txt", "r") 
    for rivi in f:
        data.append(rivi.strip())


def lue():
    global rivi
    montako_samaa = 1
    edellinen = ""
    vastaus = ""
    for chr in rivi:
        #print("chr:", chr, " montako_samaa:", montako_samaa, "edellinen:", edellinen)
        if chr == edellinen:
            montako_samaa += 1
        elif edellinen != "":
            vastaus += str(montako_samaa) + edellinen
            montako_samaa = 1
        edellinen = chr
    vastaus += str(montako_samaa) + edellinen
    rivi = vastaus

readfile()
for i in range(50):
    lue()

print(len(rivi))
