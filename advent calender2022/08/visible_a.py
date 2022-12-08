data = []
visible = 0

def readfile():   # a-kohta
    global visible
    f = open("data.txt", "r") # a-kohta !!!!      
    for rivi in f:
        data.append(rivi.strip()) 

    
def kasittele():
    global visible
    for rivi in range(len(data)):
        print("rivi", rivi)
        if rivi == 0 or rivi == len(data) - 1:  # eka ja vika rivi
            visible += len(data[rivi])
        else:
            for i in range(len(data[rivi])):
                if i == 0 or i == len(data[rivi]) - 1:  #reunat
                    visible += 1
                else:
                    # vasemmalla
                    ar = [ch for ch in data[rivi][:i] if ch >= data[rivi][i]]
                    if len(ar) == 0:                        
                        visible += 1 
                        print(rivi, i, "vas")                    

                    # oikealla"
                    else:
                        ar = [ch for ch in data[rivi][i+1:] if ch >= data[rivi][i]]
                        if len(ar) == 0:
                            visible += 1   
                            print(rivi, i, "oik")  

                        # ylh.
                        else:
                            s = muodosta_sarake(i)
                            ar = [ch for ch in s[:rivi] if ch >= s[rivi]]
                            if len(ar) == 0:
                                visible += 1  
                                print(rivi, i, "ylh")  
                            
                            # alh.
                            else:
                                s = muodosta_sarake(i)
                                ar = [ch for ch in s[rivi + 1:] if ch >= s[rivi]]
                                if len(ar) == 0:
                                    visible += 1  
                                    print(rivi, i, "alh")    

def muodosta_sarake(i):
    return [rivi[i] for rivi in data]


readfile()
kasittele() 
print(visible)      # 1676      