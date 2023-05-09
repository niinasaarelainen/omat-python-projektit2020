
data = []
dic = {}



def readfile():
    f = open("data.txt", "r") 
    for rivi in f:
        rivi = rivi.strip()
        data.append(rivi)


def muodostaSanat():
    lailliset = 0
    for rivi in data:
        moodi = "ulkona"   #   = alku
        ulkona = ""
        ulkona_array = []
        hypernet = ""
        hypernet_array = []
        for kirjain in rivi:
            if kirjain == "[":
                moodi = "hypernet"
                ulkona_array.append(ulkona)    
                ulkona = ""
            elif kirjain == "]":
                moodi = "ulkona"
                hypernet_array.append(hypernet)
                hypernet = ""
            elif moodi == "ulkona":
                ulkona += kirjain
            elif moodi == "hypernet":
                hypernet += kirjain

        ulkona_array.append(ulkona)    
        #hypernet_array.append(hypernet)

        print(ulkona_array, hypernet_array)

        lailliset += tutki(ulkona_array, hypernet_array)
    return lailliset
      
def tutki(ulkona_array, hypernet_array):

    hypers = []

    for hypernet in hypernet_array:
        for i in range(len(hypernet)-2):
            if(hypernet[i] == hypernet[i+2] and hypernet[i] != hypernet[i+1]):
                hypers.append(hypernet[i] + hypernet[i+1] + hypernet[i+2])

    for ulkona in  ulkona_array:
        for hyper in hypers:
            hyper = hyper[1] + hyper[0] + hyper[1]
            if hyper in ulkona:
                return 1
    
    return 0


readfile()
print(data)
print(muodostaSanat())  # 112 too high

