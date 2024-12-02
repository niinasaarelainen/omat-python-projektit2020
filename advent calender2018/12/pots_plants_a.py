
data = []
initial_state = "##.#....#..#......#..######..#.####.....#......##.##.##...#..#....#.#.##..##.##.#.#..#.#....#.#..#.#"
initial_state = "...#..#.#..##......###...###..........."
next_state = ""

def readfile():
    global syote
    f = open("data_1.txt", "r") 
    for rivi in f:
        sp = rivi.strip().split(" => ")
        data.append(sp)


def etsi():
    global next_state
    next_state = initial_state
    for rivi in data:
        
        ind = 0
        ohje = rivi[0]
        print("ohje  ", ohje)
        montako_sekvenssia_mahtuu = len(initial_state) // len(ohje)
        print(montako_sekvenssia_mahtuu)
        for i in range(montako_sekvenssia_mahtuu):
            alkuind = i * len(ohje)
            if ohje in initial_state[alkuind: alkuind + 6]:
                print("hep")
                next_state = initial_state[:alkuind + 3] + "#" + initial_state[alkuind + 4:]    # 2 = C  (LLCRR) 

        print(next_state)


"""
 0: ...#..#.#..##......###...###...........
 1: ...#...#....#.....#..#..#..#...........
 2: ...##..##...##....#..#..#..##..........
 """
 

readfile()
print(data)
print(initial_state)
for times in range(3):
    etsi()