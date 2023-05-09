
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

    for hypernet in hypernet_array:
        for i in range(len(hypernet)-3):
            if(hypernet[i]+ hypernet[i+1] == hypernet[i+3] + hypernet[i+2]):
                return 0

    for alku in  ulkona_array:
        for i in range(len(alku)-3):
            if(alku[i]+ alku[i+1] == alku[i+3] + alku[i+2] and not (alku[i] == alku[i+1] and alku[i+1] == alku[i+2] and alku[i+2] == alku[i+3])):
                return 1
    
    return 0


readfile()
print(data)
print(muodostaSanat())  # 112 too high