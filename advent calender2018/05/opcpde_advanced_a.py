
data = []
opcodes = [1, 2, 3, 4, 99]
"""
Opcode 3 takes a single integer as input and saves it to the position given by its only parameter. 
For example, the instruction 3,50 would take an input value and store it at address 50.

Opcode 4 outputs the value of its only parameter. 
For example, the instruction 4,50 would output the value at address 50.

3,0,4,0,99 outputs whatever it gets as input, then halts.
"""


def readfile():
    f = open("data.txt", "r") 
    for rivi in f:
        sp = rivi.split(",")
        for nro in sp:
            data.append(int(nro.strip()))


def ():
   
    return luvut



readfile()
print()
 