data = []
visible_all = []

def readfile():   # a-kohta
    global visible
    f = open("data.txt", "r") # a-kohta !!!!      
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
                ei_enaa = False
                if i == 0 or i == len(data[rivi]) - 1:  #reunat
                    pass
                else:
                    #print("\n rivi, i:", rivi, i)
                    # vasemmalla
                    for ch in reversed(data[rivi][:i]):  
                        #print("ch , data[rivi][:i]", ch ,  data[rivi][:i])                      
                        if ch < data[rivi][i] and ei_enaa == False:
                            visible_v += 1    
                        elif ei_enaa == False:
                            visible_v += 1                            
                            ei_enaa = True                          
                        
                    # oikealla"    
                    ei_enaa = False
                    for ch in data[rivi][(i+1):]:
                        #print("oike", ch)
                        if ch < data[rivi][i] and ei_enaa == False:
                            visible_o += 1  
                        elif ei_enaa == False:
                            visible_o += 1 
                            ei_enaa = True               
                        
                    #ylh
                    ei_enaa = False
                    s = muodosta_sarake(i)
                    for ch in reversed(s[:rivi]):
                        if ch < s[rivi] and ei_enaa == False:
                            visible_y += 1   
                        elif ei_enaa == False:
                            visible_y += 1 
                            ei_enaa = True              
                        
                    #alh
                    ei_enaa = False
                    s = muodosta_sarake(i)
                    for ch in s[rivi + 1:]:
                        
                        if ch < s[rivi] and ei_enaa == False:
                            visible_a += 1  
                        elif ei_enaa == False:
                            visible_a += 1 
                            ei_enaa = True   
                   

                    
                    #print(visible_v, visible_o , visible_y , visible_a)
                    tulo = visible_a  * visible_o * visible_v * visible_y
                    #print("tulo, rivi, i: ", tulo, rivi, i)
                    visible_all.append(tulo)

def muodosta_sarake(i):
    return [rivi[i] for rivi in data]


readfile()
kasittele() 
print(max(visible_all))     