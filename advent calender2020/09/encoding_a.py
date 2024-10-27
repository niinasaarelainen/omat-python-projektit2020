data = []
n_numbers = []
n = 5    # vaihda !!!!!!!!!!!!


def readfile():  
    f = open("data_2.txt", "r")         
    for rivi in f:
        data.append(int(rivi.strip()))
    print(data)
   

def validOrNot():
    global data, n_numbers
    for i in range(n, len(data)):
        ind = i - 5
        jatketaan = True
        loytyi = False        
        while jatketaan:     
            print("i", i, "data[i]", data[i])       
            if data[i] - data[ind] in data and data[ind] != data[i] - data[ind] :
                jatketaan = False  
                loytyi = True     
            if ind < n:  
                #print(ind)       
                ind += 1
            else:
                jatketaan = False  
        if not loytyi:
            print("   ei loytynyt", data[i])   # 127 ei pidä löytyä    TODO  576 !!!



readfile()
n_numbers = data[:n]
print(n_numbers)
validOrNot()