data = []
n_numbers = []
n = 25    # vaihda !!!!!!!!!!!!


def readfile():  
    f = open("data.txt", "r")         
    for rivi in f:
        data.append(int(rivi.strip()))
    print(data)
   

def validOrNot():
    global data, n_numbers
    for i in range(n, len(data)):
        ind = i - n
        jatketaan = True
        loytyi = False    
        tee_n_kertaa = 0    
        while jatketaan:     
            #print("i", i, "data[i]", data[i])       
            if data[i] - data[ind] in data[i-n:i+1] and data[ind] != data[i] - data[ind] :
                jatketaan = False  
                loytyi = True     
            if tee_n_kertaa  < n:  
                #print(ind)       
                ind += 1
                tee_n_kertaa += 1
            else:
                jatketaan = False  
        if not loytyi:
            return data[i]
            



readfile()
n_numbers = data[:n]
print(n_numbers)
print(validOrNot())