
number_of_elves = 3018458   # puzzle input
number_of_elves = 15511
presents = []


def jaa_lahjat():
    for i in range(number_of_elves):
        presents.append([i, 1])

def find():
    for olisi_vuorossa in range(number_of_elves):
        if len(presents) == 1:
            break
        i = int(len(presents)  / 2) 
        tonttu_array = [tonttu  for tonttu in presents if tonttu[0]== olisi_vuorossa]
        if tonttu_array != []:
            tonttu = tonttu_array[0]
            vuorossa_ind = presents.index(tonttu)
            #print("vuorossa", vuorossa_ind)
            if tonttu in presents:  
                #print("(vuorossa_ind + i) % len(presents)", (vuorossa_ind + i) % len(presents))
                #print("presents[(vuorossa_ind + i) % len(presents)][1]", presents[(vuorossa_ind + i) % len(presents)][1])
                presents[vuorossa_ind][1] += presents[(vuorossa_ind + i) % len(presents)][1]
                del presents[(vuorossa_ind + i) % len(presents)] 
                #print(presents)  


jaa_lahjat()
#print(presents)
#for i in range(3018458 * 2):
find() 
find()
find()
    

print(presents[0][0] + 1)
    
    


