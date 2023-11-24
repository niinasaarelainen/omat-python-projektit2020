import random

a_dict = {'R': 'Red', 'B': 'Black', 'P': 'Pink'} 
b_dict = {'G': 'Green', 'W': 'White'}

# print(a.union(b)) ei käy

# TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
# a + b
a_dict.update(b_dict)
print(a_dict)

a = {'R': 'Red', 'B': 'Black', 'P': 'Pink'} 
ab = a.items()  | a_dict.items() 

print(ab)

a = [1, 2, 3]
b = [3, 4]
c = a + b
print(c)


for x in range(10):
    i  = random.randint(0, 20)
    if chr(65 + i) in a_dict:
        print(a_dict[chr(65 + i)])


