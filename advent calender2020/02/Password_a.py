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
        montako, mita = rule.split(" ")
        montako_min, montako_max = montako.split("-")
        print("input.count", mita,  input.count(mita))
        if int(montako_min) <= input.count(mita) <= int(montako_max):
            valid += 1
    
    print(valid)
    print(len(rule_input))


readfile()
rule_input_read()