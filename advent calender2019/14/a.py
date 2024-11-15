
data = []
hash = {}
hash_toisinpain = {}
ore_summa = 0


def readfile():
    global data
    f = open("data_1.txt", "r") 
    for rivi in f:
        data.append(rivi.strip())


def tee_hash():
    for rivi in data:
        a, b = rivi.split(" => ")  # 7 A, 1 B => 1 C
        maara, symboli = b.split(" ")
        if "," in a:
            l = tuple(a.split(", "))
            hash[l] = b
            hash_toisinpain[symboli] = [l, maara]
        else:
            hash[a] = b
            maara, kirjain = b.split(" ")
            hash_toisinpain[symboli] = [a, maara]
    

def kay_lapi(k):
    key_nyt = k
    value_nyt = hash_toisinpain[key_nyt]

    if "ORE" not in value_nyt :
        return
    value_nyt = hash_toisinpain[key_nyt]
    print(value_nyt)
    for item in value_nyt:
        kay_lapi(item.split(" ")[1])


    print("ulkona")



readfile()
tee_hash()
print("\nhash", hash)
print("\nhash_toisinpain", hash_toisinpain)
kay_lapi(hash_toisinpain["FUEL"])