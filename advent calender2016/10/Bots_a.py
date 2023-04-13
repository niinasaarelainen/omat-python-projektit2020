import copy

data = []
bots = {}
outputs = {}

def readfile():
    global data
    f = open("data.txt", "r") 
    for rivi in f:
        data.append(rivi.strip().split(" "))


def value_komennot():
    global data, bots
    for rivi in data:  
        if "value" in rivi:
            bot_nro = int(rivi[5])
            val = int(rivi[1])
            if bot_nro in bots:
                bots[bot_nro].append(val)
            else:
                bots[bot_nro] = [val]

def gives_komennot():   # 'bot', '2', 'gives', 'low', 'to', 'bot/output', '1', 'and', 'high', 'to', 'bot/output', '0'
    global data, bots   #  0      1     2       3             5             6            8       9      10        11
    data2 = copy.deepcopy(data)
    for rivi in data:  
        if "gives" in rivi:            
            bot_giver = int(rivi[1])
            if bot_giver not in bots:
                continue
            elif len(bots[bot_giver]) != 2:
                continue
            else:
                data2.remove(rivi)
            lower_id = int(rivi[6])
            higher_id = int(rivi[11])
            vals = bots[bot_giver]
            if 61 in vals and 17 in vals:
                print(bot_giver, "!!!!")
            bots[bot_giver] = []
            low = min(vals)
            high = max(vals)

            if rivi[5] == "bot":
                if lower_id in bots:
                    bots[lower_id].append(low)
                else:
                    bots[lower_id] = [low]
            if rivi[5] == "output":
                if lower_id in outputs:
                    outputs[lower_id].append(low)
                else:
                    outputs[lower_id] = [low]    

            if rivi[10] == "bot":
                if higher_id in bots:
                    bots[higher_id].append(high)
                else:
                    bots[higher_id] = [high]
            if rivi[10] == "output":
                if higher_id in outputs:
                    outputs[higher_id].append(high)
                else:
                    outputs[higher_id] = [high]    
    
    
    data = copy.deepcopy(data2)
    #print(bots)
    

readfile()
value_komennot()
for i in range(29):
    gives_komennot()
