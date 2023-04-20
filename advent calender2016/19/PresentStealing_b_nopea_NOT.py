
number_of_elves = 3018458   # puzzle input
#number_of_elves = 15
presents = []
zero_elves = 0
present_elves = number_of_elves


def jaa_lahjat():
    for i in range(number_of_elves):
        presents.append(1)

def find():
    global zero_elves, present_elves
    for vuorossa in range(number_of_elves):
        if zero_elves == number_of_elves - 1:            
            break

        if presents[vuorossa] != 0:
            #print("vuorossa: ", vuorossa)
            puolivali = int(present_elves / 2) 
            laskuri_all = 0
            laskuri_ei_zerot = 0

            while laskuri_ei_zerot < puolivali:
                #print(laskuri_ei_zerot, puolivali)
                laskuri_all += 1
                if presents[(vuorossa + laskuri_all) % number_of_elves] != 0:                    
                    laskuri_ei_zerot += 1
                

            presents[vuorossa] += presents[(vuorossa + laskuri_all) % number_of_elves]
            presents[(vuorossa + laskuri_all) % number_of_elves] = 0
            zero_elves += 1
            #print("zero_elves", zero_elves)
            present_elves -= 1   # käytä tätä !!!!! ei toista for-luuppia !
        #print(presents)


jaa_lahjat()
#for i in range(3018458 * 2):
for i in range(3):
    find() 
    print("välikalja")

print(presents.index(number_of_elves) + 1)
    
    


