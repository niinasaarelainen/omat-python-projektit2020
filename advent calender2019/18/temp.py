

# löytää vain samalta riviltä

def find_2_lahinta(y, x):
    lahimmat_avaimet = {}  # avaimen x : askeleet @:sta

    # oikealle:
    if x < len(data[y]) -1:
        for merkki in range(x +1, len(data[y])):            
            if data[y][merkki] in ['.', '#']:
                pass 
            elif data[y][merkki].islower():
                lahimmat_avaimet[(data[y][merkki])] = abs(merkki - x)
                break
            else: 
                break

    # vasemmalle
    if x > 0:
        for merkki in range(x - 1, -1, -1):
            if data[y][merkki] in ['.', '#']:
                pass 
            elif data[y][merkki].islower():
                lahimmat_avaimet[(data[y][merkki])] = abs(merkki - x)
                break
            else:
                break

    return lahimmat_avaimet