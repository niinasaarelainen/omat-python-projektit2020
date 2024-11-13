def oma_sum_of_list(nro, ind, summa=0):
    summa += nro
    if  ind == 0:        
        return summa
    else:
        ind -= 1
        return oma_sum_of_list(l[ind], ind, summa)


def list_sum(num_List):
    # Check if the length of the input list is 1
    if len(num_List) == 1:
        # If the list has only one element, return that element
        return num_List[0]
    else:
        # If the list has more than one element, return the sum of the first element
        # and the result of recursively calling the list_sum function on the rest of the list
        return num_List[0] + list_sum(num_List[1:])


def sum_recursion_lists(value, l):    # ei toimi
    print(value, l) 
    if len(l) == 1:
        return value
    elif isinstance(value, list):                    
        return sum_recursion_lists(value[0], value)  
    else:
        print("else", value) 
        # If the list has more than one element, return the sum of the first element
        # and the result of recursively calling the list_sum function on the rest of the list
        return l[0] + sum_recursion_lists(l[1:][0], l[1:])


# huom!! for-luuppi ja rekursio ja str
def recursive_list_sum(data_list):
    str = ""
    
    # Iterate through each element in the input list
    for element in data_list:
        # Check if the current element is a list (nested list)
        if type(element) == type([]):
            
            # If the element is a list, recursively call the recursive_list_sum function on the element
            str = str + recursive_list_sum(element)
            sanat.append(str)
            #return ""
        elif type(hash[element]) == type([]):
            print("moi")   # miksi vian kerran !?!?!?!
            str = str + recursive_list_sum(hash[element])
            sanat.append(str)
        else:
            # If the element is not a list, add its value to the str
            str = str + hash[element]
            sanat.append(str)
    
    return str




l = [1,2,3]
ind = len(l) - 1
#print(oma_sum_of_list(l[ind], ind))

#print(list_sum(l))

l = [1, 2, 4]
hash = {1: "a", 2: "b", 3: "c", 4:[[1,2], [3,1]]}
#hash = {1: "a", 2: "b", 3:[2,1]}
#l = [1, 2, [3,4], 5]
#print(sum_recursion_lists(l[0], l))  # ei toimi

sanat = []
recursive_list_sum(l)
print(sanat)