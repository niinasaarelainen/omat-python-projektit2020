data = []
str = "HASH"
value = 0
values = []


def readfile():   
    f = open("data.txt", "r")         
    for rivi in f:           
        sp = rivi.strip().split(",")
        for item in sp:
            data.append(item)   # jos laittaa suoraan sp, tulee  [[

    

def tutki_str():
    global value
    for item in data:
        value = 0
        for letter in item:
            value += ord(letter)
            value *= 17
            value = value % 256

        values.append(value)

            


readfile()   
print(data)
value = tutki_str()
print(sum(values))
