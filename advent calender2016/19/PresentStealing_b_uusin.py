
number_of_elves = 3018458   # puzzle input
#number_of_elves = 5
presents = []


def jaa_lahjat():
    for i in range(number_of_elves):
        presents.append([i, 1])

def find():
    olisi_vuorossa = 0
    while olisi_vuorossa < number_of_elves:
        if len(presents) == 1:
            break
        if olisi_vuorossa > len(presents):
            olisi_vuorossa = 0
        i = int(len(presents)  / 2) 
        if presents[olisi_vuorossa % len(presents)] != 0:
            #print("olisi_vuorossa", olisi_vuorossa)
            #print("olisi_vuorossa% len(presents", olisi_vuorossa% len(presents))
            presents[olisi_vuorossa% len(presents)][1] += presents[(olisi_vuorossa + i) % len(presents)][1]
            del presents[(olisi_vuorossa + i) % len(presents)] 
            #print(presents, "\n")  
        olisi_vuorossa += 1
        


jaa_lahjat()
find()     

print(presents[0][0] + 1)   # 6437 too low
    
    


