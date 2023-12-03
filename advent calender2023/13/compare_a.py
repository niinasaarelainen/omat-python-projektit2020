import ast

data = []
right_order = 0


def readfile():   
    f = open("data_1.txt", "r")         
    for rivi in f:
        if rivi.strip() != "":           
            data.append(rivi.strip())


def compare():
    global right_order
    ran_out_of_items = False  # TODO Left side ran out of items, so inputs are in the right order
    for ind in range(0, len(data), 2):
        eka = ast.literal_eval(data[ind])
        if not isinstance(eka, list):
            eka = [eka]
        toka = ast.literal_eval(data[ind + 1])
        if not isinstance(toka, list):
            toka = [toka]

        for i in range(min(len(eka), len(toka))):
            if not isinstance(eka[i], list):
                eka[i] = [eka[i]]
            if not isinstance(toka[i], list):
                toka[i] = [toka[i]]
            if eka[i] < toka[i]:
                print(eka[i], toka[i])
                right_order += 1
                return

        


readfile()    # datassa 10
print(data)
compare()
print("right_order", right_order)


"""
if isinstance([5], list):
    print("list") 
    
print([[2,3,5]] < [[2,3,4]])"""