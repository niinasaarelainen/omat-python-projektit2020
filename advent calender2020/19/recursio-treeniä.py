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


def recursive_listsum(data_list):   # NETISTÄ
    total = 0
    
    # Iterate through each element in the input list
    for element in data_list:
        # Check if the current element is a list (nested list)
        if type(element) == type([]):
            # If the element is a list, recursively call the recursive_list_sum function on the element
            total = total + recursive_listsum(element)
        else:
            # If the element is not a list, add its value to the total
            total = total + element
    
    return total


# huom!! for-luuppi ja rekursio ja str
def recursive_list_sum(data_list):   # OMA   EI TOIMI"
    str = ""
    
    # Iterate through each element in the input list
    for element in data_list:
        # Check if the current element is a list (nested list)
        if type(element) == type([]):            
            # If the element is a list, recursively call the recursive_list_sum function on the element
            str = str + recursive_list_sum(element)
            sanat.append(str)
            #return ""
        if type(hash1[element]) == type([]):
            str = str + recursive_list_sum(hash1[element])
            sanat.append(str)
            #str = ""
        if type(hash2[element]) == type([]):
            print("hash2")
            str = str + recursive_list_sum(hash2[element])
            sanat.append(str)
            str = ""
        if type(hash1[element]) != type([]): 
            # If the element is not a list, add its value to the str
            str = str + hash1[element]
    
    return str


def factorial(luku):
    if luku == 1:
        return 1
    else:
       return luku * factorial(luku - 1) 

def fibonacci (l, raja):
    if l[-1] >= raja:
        return l

    else:
        l.append(l[-1] + l[-2])
        return fibonacci(l, raja)
    

def sum_series(luku):
    if luku == 0:
        return luku
    else:
       return luku + sum_series(luku - 2) 


def sum_of_harmonic_series(luku, raja):  # OMA, huom! ei tarvita alustusta sum = 0.0, koska summa kerääntyy elsessä

    if luku == raja:
        return 1 / luku
    else:
        return  1 / luku + sum_of_harmonic_series(luku + 1, raja)


def harmonic_sum(n):  # ONLINE
    if n < 2:
        return 1
    else:
        return 1 / n + harmonic_sum(n - 1)


def power(a, b):  # a potensssiin b
    if b == 1:
        return a
    else:
        return a * power(a, b-1) 


ok = []
def greatest_common_divisor(i1, i2, jakaja):
    
    if i1 % jakaja == 0 and i2 % jakaja == 0:  
            ok.append(jakaja)   
    
    if jakaja == min(i1, i2):          
        return max(ok)
    else:
        return greatest_common_divisor(i1, i2, jakaja + 1)



l = [1,2,3]
ind = len(l) - 1
#print(oma_sum_of_list(l[ind], ind))

nro = 345
l = [int(c) for c in str(nro)]
print(l)
print(list_sum(l))

l = [1, 2, 4]
hash1 = {1: "a", 2: "b", 3: "c", 4:[1,2]}
hash2 = {1: "a", 2: "b", 3: "c", 4:[3,1]}
#hash = {1: "a", 2: "b", 3:[2,1]}
#l = [1, 2, [3,4], 5]
#print(sum_recursion_lists(l[0], l))  # ei toimi

sanat = []
recursive_list_sum(l)
print(sanat)

l= [1, 2, [3,4], [5,6]]
print(recursive_listsum(l))

print(factorial(4))

print(fibonacci([0,1], 2000))

print(sum_series(10))

print(sum_of_harmonic_series(1, 4))
print(harmonic_sum(4))

print(power(3,4))

i1 = 21
i2 = 18
print(greatest_common_divisor(i1, i2, 1))  # 1 = pienin jakaja