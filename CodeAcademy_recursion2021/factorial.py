
# malli
def factorial(x):

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))

print("The factorial of", 3, "is", factorial(3))
print("The factorial of", 4, "is", factorial(4))
print("The factorial of", 6, "is", factorial(6))




# oma
def factorial_oma(x):
    if x == 1:
        return x
    
    x -= 1
    return factorial_oma(x) * (x + 1)
    
print(factorial_oma(3))  # 6
print(factorial_oma(4))  # 10
print(factorial_oma(6))  # 21


# oma
def sum_oma(x):
    if x == 1:
        return x
    
    x -= 1
    return sum_oma(x) + x + 1
    
print(sum_oma(3))  # 6
print(sum_oma(4))  # 10
print(sum_oma(6))  # 21


def sum_oma2(x):
    if x == 1:
        return x
   
    return sum_oma2(x- 1) + x 
    
print(sum_oma2(3))  # 6
print(sum_oma2(4))  # 10
print(sum_oma2(6))  # 21


def sum_oma_parilliset(x):
    if x == 2:
        return x
   
    return sum_oma_parilliset(x - 2) + x 
    
print("sum_oma_parilliset", sum_oma_parilliset(4))  # 6
print(sum_oma_parilliset(6))  # 12
print(sum_oma_parilliset(8))  # 20


def print_parilliset(x):
    if x == 2:
        print(x)
        return 
    print(x)
    return print_parilliset(x - 2) 
    
print("sum_oma_parilliset", sum_oma_parilliset(4))  # 6
print(sum_oma_parilliset(6))  # 12
print(sum_oma_parilliset(8))  # 20

print()
print_parilliset(18)
