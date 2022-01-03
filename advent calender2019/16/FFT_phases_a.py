
data = []
base_pattern = [0, 1, 0, -1]
phases = []
syote = ""


def readfile():
    global syote
    f = open("data.txt", "r") 
    for rivi in f:
        data.append(rivi.strip())
    syote = data[0]


def laske_base_pattern(montako):
    base_pattern_nykyinen = []
    for ind in range(len(data[0]) +1):  # tehdään 1 liian pitkä jotta shiftin jälkeen voi katkaista
        ind = ind % 4
        for i in range(montako):            
            base_pattern_nykyinen.append(base_pattern[ind])
    
    base_pattern_nykyinen = base_pattern_nykyinen[1:len(data[0])+1]

    return base_pattern_nykyinen




def phase():
   base_pattern_nykyinen = []
   summa = 0
   summat = []
   
   for montako in range(len(data[0])):
       summa = 0
       base_pattern_nykyinen = laske_base_pattern(montako + 1)
       for i in range(len(syote)):
           summa += int(syote[i]) * base_pattern_nykyinen[i]

       summat.append(str(summa)[-1])

   return ''.join(summat)



readfile()

for i in range(100):   # 74608727
    syote = phase()
    print(syote)
