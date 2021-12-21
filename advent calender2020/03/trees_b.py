
# open squares (.) and trees (#)

data = []
montako_list = []
ohjeet = [[1,1],[3,1],[5,1],[7,1],[1,2]]

"""
1, down 1.
Right 3, down 1. (This is the slope you already checked.)  a-osassa
Right 5, down 1.
Right 7, down 1.
Right 1, down 2   """


def readfile():
    f = open("data.txt", "r")         
    for rivi in f:
        data.append(rivi.strip())   


def etsi_puut(x_orig, y_orig):
    montako = 0
    x = x_orig
    y = y_orig
    for i in range((len(data) -1)//y ):
        print("i", i, "y", y)
        if data[y][x] == "#":
            montako += 1
        x += x_orig
        if x >= len(data[0]):
            x -= len(data[0]) 
        y += y_orig
    montako_list.append(montako)



readfile()
for x, y in ohjeet:
    etsi_puut(x, y)

print(montako_list)

vastaus = 1
for luku in montako_list:
    vastaus *= luku
print(vastaus)