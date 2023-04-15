
wanted_str = "00101000101111010"   # oikea
#wanted_str = "10000"


def muunna(str): 
    uusi_rivi = ""
    for letter in str:
        if letter == "0":
            uusi_rivi += "1"
        if letter == "1":
            uusi_rivi += "0"
    uusi_rivi = uusi_rivi[::-1]
    #print(uusi_rivi)
    return str + "0" + uusi_rivi


def checksum(st):
    ch_sum = ""
    if len(st) % 2 == 0:
        i = 0
        for times in range(int(len(st) / 2)):
            if st[i] == st[i+1]:
                ch_sum += "1"
            else:
                ch_sum += "0"
            i += 2
    if len(ch_sum) % 2 == 0:
        checksum(ch_sum)
    else:
        print(ch_sum)
    


print(wanted_str)
while len(wanted_str) < 35651584:
    wanted_str = muunna(wanted_str)[:35651584]

print(len(wanted_str))
# s = "".join(str(x) for x in stringi)
checksum(wanted_str)

