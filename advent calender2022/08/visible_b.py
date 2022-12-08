data = []
visible_all = []

def readfile():   # a-kohta
    global visible
    f = open("data_a.txt", "r") # a-kohta !!!!      
    for rivi in f:
        data.append(rivi.strip()) 

    
def kasittele():
    global visible
    for rivi in range(len(data)):
        visible = 0        
        if rivi == 0 or rivi == len(data) - 1:  # eka ja vika rivi
            pass    # reunoilta tuskin löytyy max
        else:
            for i in range(len(data[rivi])):
                visible_v = 0
                visible_o = 0
                visible_y = 0
                visible_a = 0
                if i == 0 or i == len(data[rivi]) - 1:  #reunat
                    pass
                else:
                    # vasemmalla
                    for ch in data[rivi][:i]:  
                        print("ch , data[rivi][:i]", ch ,  data[rivi][:i])                      
                        if ch <= data[rivi][i]:
                            visible_v += 1                              
                        
                    # oikealla"    # array  reversed !?!?!?!?!?!!?
                    for ch in data[rivi][(i+1):]:
                        #print("ch , data[rivi][i+1:]", ch ,  data[rivi][(i+1):])
                        if ch <= data[rivi][i]:
                            visible_o += 1              
                        
                    #ylh
                    s = muodosta_sarake(i)
                    for ch in s[:rivi]:
                        if ch <= s[rivi]:
                            visible_y += 1               
                        
                    #alh
                    s = muodosta_sarake(i)
                    for ch in s[rivi + 1:]:
                        if ch <= s[rivi]:
                            visible_a += 1   
                   

                    print(visible_v, visible_o , visible_y , visible_a)
                    tulo = visible_a * visible_o * visible_v * visible_y
                    print("tulo, rivi, i: ", tulo, rivi, i)
                    visible_all.append(visible)

def muodosta_sarake(i):
    return [rivi[i] for rivi in data]


readfile()
kasittele() 
print(visible)      # 1676      