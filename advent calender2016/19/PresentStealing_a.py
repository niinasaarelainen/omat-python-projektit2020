
number_of_elves = 3018458   # puzzle input
#number_of_elves = 15511
presents = []
zero_elves = 0


def jaa_lahjat():
    for i in range(number_of_elves):
        presents.append(1)

def find():
    global zero_elves
    for vuorossa in range(number_of_elves):
        if zero_elves == number_of_elves - 1:
            break
        if presents[vuorossa] != 0:
            i = 1
            while presents[(vuorossa + i) % number_of_elves] == 0:
                i += 1
            presents[vuorossa] += presents[(vuorossa + i) % number_of_elves]
            presents[(vuorossa + i) % number_of_elves] = 0
            zero_elves += 1
        


jaa_lahjat()
#print(presents)
#for i in range(3018458 * 2):
for i in range(number_of_elves*2):
    find() 

print(presents.index(number_of_elves) + 1)
    
    


