
data = []  # free  0 .   used  1 #

"""
##.#.#..-->   flqrgnkx-0
.#.#.#.#      flqrgnkx-1
....#.#.   
#.#.##.#   
.##.#...   
##..#..#   
.#...#..   
##.#.##.-->
|      |   
V      V                 """ 

def readfile():
    f = open( "data_a.txt", "r") 
    for rivi in f:
        rivi = rivi.strip()
        data.append(rivi)


def find():
    global data


readfile()
find() 
#print(format(e,'04b')) 
x = "e"
print(f'{x:08b}') 
    
    


