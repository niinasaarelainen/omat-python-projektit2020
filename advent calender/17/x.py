import math

crabs = []


def readfile():   # a-kohta
    global crabs
    f = open("data.txt", "r")         
    for rivi in f:
        numerot_str = rivi.split(",")
        for nro in numerot_str:
            crabs.append(int(nro))
    print(crabs)


def least_fuel():  # 1-part
    mi = min(crabs)
    ma = max(crabs)
    fuel = 0
    fuel_min = None

    for point in range(mi, ma):
        fuel = 0
        for crab in crabs:
            fuel += abs(crab - point)
            
        if fuel_min == None:
            fuel_min = fuel
        elif fuel < fuel_min:
            fuel_min = fuel
        print("fuel_min", fuel_min)


def least_fuel2():   # b-part   92676646 oik.vast
    mi = min(crabs)
    ma = max(crabs)
    fuel = 0
    fuel_min = None

    for point in range(mi, ma):
        fuel = 0
        for crab in crabs:
            valimatka = abs(crab - point)
            for i in range(valimatka + 1):
                fuel += i
            
        if fuel_min == None:
            fuel_min = fuel
        elif fuel < fuel_min:
            fuel_min = fuel

    print("fuel_min", fuel_min)    



readfile()
least_fuel2()
