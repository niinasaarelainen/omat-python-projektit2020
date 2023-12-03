import math

data = []
x = 6
y = x
ar = []
H_x = 0   # start of head
H_y = 5
T_x = 0   # start of tail
T_y = 5
T_visited = [(T_y, T_x)]


def readfile():   # a-kohta
    f = open("data_a1.txt", "r")         
    for rivi in f:
        data.append(rivi.strip().split(" "))
    print(data)

def luo_array():
    global ar, x, y
    for i in range(x):
        ar.append([])
        for j in range(y):
            ar[i].append(".")
    


def liiku():   
    global H_x, H_y, T_x, T_y, T_visited
    for rivi in data:
        maara = int(rivi[1])
        if "L" in rivi:
            for i in range(maara):                
                H_x -= 1
                ar[H_y][H_x] = "H"
                if abs(H_x - T_x) == 2 and abs(H_y - T_y) == 0:
                    T_x -= 1
                if abs(H_x - T_x) == 2 and abs(H_y - T_y) == 1:
                    T_y = H_y
                    T_x -= 1
                if (T_y, T_x) not in T_visited:
                    T_visited.append((T_y, T_x))
                ar[T_y][T_x] = "T"

        if "R" in rivi:
            for i in range(maara):                
                H_x += 1
                print(H_x)
                ar[H_y][H_x] = "H"
                if abs(H_x - T_x) == 2 and abs(H_y - T_y) == 0:
                    T_x += 1
                if abs(H_x - T_x) == 2 and abs(H_y - T_y) == 1:
                    T_y = H_y
                    T_x += 1
                if (T_y, T_x) not in T_visited:
                    T_visited.append((T_y, T_x))
                ar[T_y][T_x] = "T"

        if "U" in rivi:
            for i in range(maara):                
                H_y -= 1
                ar[H_y][H_x] = "H"                
                if abs(H_y - T_y) == 2 and abs(H_x - T_x) == 0:
                    T_y -= 1
                elif abs(H_y - T_y) == 2 and abs(H_x - T_x) == 1:
                    T_y -= 1
                    T_x = H_x
                if (T_y, T_x) not in T_visited:
                    T_visited.append((T_y, T_x))
                ar[T_y][T_x] = "T"

        if "D" in rivi:
            for i in range(maara):                
                H_y += 1
                ar[H_y][H_x] = "H"                
                if abs(H_y - T_y) == 2 and abs(H_x - T_x) == 0:
                    T_y += 1
                elif abs(H_y - T_y) == 2 and abs(H_x - T_x) == 1:
                    T_y += 1
                    T_x = H_x
                if (T_y, T_x) not in T_visited:
                    T_visited.append((T_y, T_x))
                ar[T_y][T_x] = "T"


        for rivi in ar:
            print(rivi)
        print()


"""
..##..
...##.
.####.
....#.
s###..   """    
   


readfile()
luo_array()
liiku()   
print(T_visited)  
print(len(T_visited))  