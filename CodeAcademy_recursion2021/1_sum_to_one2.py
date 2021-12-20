

def sum_to_one(n):
    global result, call_stack
    name = "recursive_func_" + str(n)
    print(name)
    if n == 1:
        call_stack.append(name)   
        return result, call_stack
    call_stack.append(name)  
    result += n   
    n -= 1         
    result, call_stack = sum_to_one(n)
    call_stack.reverse()
    return result, call_stack
            

result = 1
call_stack = []
print(sum_to_one(4)) 



 