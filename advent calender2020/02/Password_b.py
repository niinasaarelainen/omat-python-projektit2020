data = []
rule_input = []

def readfile():
    x = 0
    aim = 0
    y = 0
    f = open("data.txt", "r") 
    for rivi in f:
        rule, input = rivi.split(":")
        rule_input.append([rule, input])
        

    print(rule_input)


def rule_input_read():
    valid = 0
    for rule, input in rule_input:
        input = input.strip()
        positions, mita = rule.split(" ")
        positions = positions.split("-")

        print("input", input)

        pos1 = int(positions[0]) - 1
        pos2 = int(positions[1]) - 1

        t1 = input[pos1] == mita
        #print("input[pos1]", input[pos1])
        t2 = input[pos2] == mita
        #print("input[pos2]", input[pos2])

        if [t1, t2].count(True) == 1:
            valid += 1
    
    print(valid)
    print(len(rule_input))


readfile()
rule_input_read()