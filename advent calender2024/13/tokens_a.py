
data = []
Prize_X = 8400   
Prize_Y = 5400
a_X = 94
a_Y = 34
b_X = 22
b_Y = 67
a_token = 3
b_token = 1

def readfile():  
    f = open("data.txt", "r")         
    for rivi in f:
        data.append(rivi.strip())


def maaritaRajat():  # A button 80 times and the B button 40 times
    ax = (Prize_X + a_X - 1 ) // a_X
    ay = (Prize_Y + a_Y - 1 ) // a_Y
    print(max(ax, ay), "a")

    bx = (Prize_X + b_X - 1 ) // b_X
    by = (Prize_Y + b_Y - 1 ) // b_Y
    print(max(bx, by), "b")


readfile()
maaritaRajat()