
data = []
nodes = {}


def readfile():   # a-kohta
    f = open("data_b.txt", "r")  
    for rivi in f:
        data.append(list(rivi.strip())) 
    

def kasittele_data():
    for y in range(len(data)):
        for x in range(len(data[0])):
            print(data[y][x], end="")
            if data[y][x] != ".":
                if data[y][x] in nodes:
                    nodes[data[y][x]].append([y, x])
                else:
                    nodes[data[y][x]] = [[y, x]]
        print()


def kasittele_nodes():
    for k in nodes:
        koordinaatit = nodes[k]
        for verrokki in range(len(koordinaatit)-1):
            for plus_yx in range(verrokki+1, len(koordinaatit)):
                y1, x1 = koordinaatit[verrokki]
                y2, x2 = koordinaatit[plus_yx]

                # y2 alempana !! :
                if y1 > y2:
                    temp = y1
                    y1 = y2
                    y2 = temp
                    temp = x1
                    x1 = x2
                    x2 = temp
                print("verrokki:", y1, x1, "verrokki + 1:", y2, x2)
                antinode1_y = y1 - (y2 - y1) 
                antinode1_x = x1 - (x2 - x1)
                print(antinode1_y, antinode1_x)
                if antinode1_y >= 0 and antinode1_y < len(data) and antinode1_x >= 0 and antinode1_x < len(data[0]):
                    data[antinode1_y][antinode1_x] = "#"

                
                antinode2_y = y2 + (y2 - y1) 
                antinode2_x = x2 + (x2 - x1)
                if antinode2_y >= 0 and antinode2_y < len(data) and antinode2_x >= 0 and antinode2_x < len(data[0]):
                    data[antinode2_y][antinode2_x] = "#" 

     


readfile()
kasittele_data() 
print(nodes)
print(kasittele_nodes() )

hashtagit = 0
for y in range(len(data)):
        for x in range(len(data[0])):
            print(data[y][x], end="")
            if data[y][x] == "#":
                hashtagit += 1
        print()

print(hashtagit)