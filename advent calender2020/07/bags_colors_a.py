

laukkujen_sisalto = {}
laukkujen_sisalto_key_on_value = {}


def readfile():   
    f = open("data.txt", "r")         
    for rivi in f:
        split1 = rivi.split(" bags contain ")
        laukkujen_sisalto[split1[0]] = split1[1].strip()  
        laukkujen_sisalto_key_on_value[split1[1].strip()] = split1[0]


def etsi():
    keys = []
    for key in laukkujen_sisalto:
        #if "shiny gold" in key:
        #    keys.append(key)
        if "shiny gold" in laukkujen_sisalto[key]:
            keys.append(key)

    for i in range(25):  # tarpeeksi monta kertaa
        keys_lisaa = []
        print("laukkujen_sisalto_key_on_value.keys()", laukkujen_sisalto_key_on_value.keys())
        for key in keys:
            for key_dict in laukkujen_sisalto_key_on_value:
                if key in key_dict:
                    print(key_dict)
                    keys_lisaa.append(laukkujen_sisalto_key_on_value[key_dict])

        for key in keys_lisaa:
            if key not in keys:
                keys.append(key)

 
    print(keys)
    print(len(keys))  





readfile()
etsi()
