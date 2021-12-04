
data = []


def readfile():
    f = open("data.txt", "r")          #TODO vaihda !!!!!!!!!!
    for rivi in f:
        data.append(rivi.strip())

def laske_gamma_ja_epsilon(maarat):
    g = ""
    e = ""
    for lkm in maarat:
        if lkm > len(data)//2:
            g += "1"
            e += "0"
        else:
            g += "0"
            e += "1"
    print(g, e)
    return g, e
    


def decode():
    gamma_rate = 0
    epsilon_rate = 0
    maarat = []
    for i in range(len(data[0])):
        maarat.append(0)
    for rivi in data:
        for i in range(len(rivi)):
            maarat[i] += int(rivi[i])
    gamma_rate, epsilon_rate = laske_gamma_ja_epsilon(maarat)
    return gamma_rate, epsilon_rate


def binary_to_decimal(b_num):
    value = 0
    b_num = list(b_num)
    for i in range(len(b_num)):
        digit = b_num.pop()
        if digit == '1':
            value = value + pow(2, i)
    return value


readfile()
g, e = decode()
g = binary_to_decimal(g)
e = binary_to_decimal(e)
print(g * e)