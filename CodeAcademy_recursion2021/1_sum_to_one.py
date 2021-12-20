
"""   eka yritys, 2 funktiota """

def recursive_func(x, result, call_stack, n):
    name = "recursive_func_" + str(x)
    print(name)
    if x == n:
        call_stack.append(name)    
        print(result, call_stack)
        return result, call_stack
    call_stack.append(name)            
    x += 1   
    result += x         
    return recursive_func(x, result, call_stack, n)


def sum_to_one(n):
    result = 1
    call_stack = []
    result, call_stack = recursive_func(1, result, call_stack, n)
    return result, call_stack
            

print(sum_to_one(4))  
 